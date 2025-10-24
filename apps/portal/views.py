# apps/portal/views.py
import logging
from django_datatables_view.base_datatable_view import BaseDatatableView

from rest_framework.decorators import action
from drf_yasg import openapi

from django.template.loader import render_to_string
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView,  DetailView

from . import models


class EntityListJson(BaseDatatableView):
    max_display_length = 100
    model = models.Entity
    columns = ['id', 'name', 'gender', 'organization', 'created_at', 'updated_at']

    def render_column(self, row, column):
        # Render the category (gender) and hierarchy (organization)
        if column == 'gender':
            # Assuming there could be multiple categories (gender), join their names
            categories = ", ".join([category.name for category in row.gender.all()])
            return categories or "Sem categoria"
        
        if column == 'organization':
            return row.organization.name if row.organization else "Sem hierarquia"

        return super(EntityListJson, self).render_column(row, column)

    

class EntityListView(TemplateView):
    template_name = 'entity_list.html'


class ComandosAPIPortalView(TemplateView):
    template_name = 'command_portal.html'


class MilitaryListJson(BaseDatatableView):
    max_display_length = 100
    model = models.Military
    columns = ['id', 'rank', 'register', 'nickname', 'name',
               'cpf', 'activity_status', 'unidade']

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'rank':
            rank = models.Promotion.objects.filter(military=row.id).last()
            row.rank = rank.rank
            return row.rank

        if column == 'unidade':
            unit = models.HistoryTransfer.objects.filter(military=row.id).last()
            row.unidade = unit.entity.name
            return row.unidade

        return super(MilitaryListJson, self).render_column(row, column)


class MilitaryListView(TemplateView):
    template_name = 'military_list.html'


class MilitaryProfileView(DetailView):
    template_name = 'profile.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        object = get_object_or_404(models.Military, id=id_)
        promotions = models.Promotion.objects.filter(military=id_)
        object.rankActual = promotions.latest('created_at')
        object.promotions = promotions

        histories = models.HistoryTransfer.objects.filter(
            military=id_)
        object.histories = histories
        object.unitActual = histories.latest('created_at').entity.name

        return object


# Get an instance of a logger
logger = logging.getLogger(__name__)

name = openapi.Parameter('name', openapi.IN_QUERY,
                                  description="param nome do militar", type=openapi.TYPE_STRING)
register = openapi.Parameter('register', openapi.IN_QUERY,
                                    description="param matrícula do militar", type=openapi.TYPE_STRING)
email = openapi.Parameter('email', openapi.IN_QUERY,
                                    description="param e-mail do militar", type=openapi.TYPE_STRING)
nickname = openapi.Parameter('nickname', openapi.IN_QUERY,
                                    description="param nome de guerra do militar", type=openapi.TYPE_STRING)
cpf = openapi.Parameter('cpf', openapi.IN_QUERY,
                        description="param número do CPF do militar", type=openapi.TYPE_STRING)


class AutocompleteMilitaryView(View):
    
    @action(detail=True, methods=['GET'])
    def get(self, request, *args, **kwargs):
        
        try:
            if self.request.user.groups.filter(name__in=['portal:military', 'portal:military_basic']).exists():
                # Retrieve the parameter from the request
                term = request.GET.get('term')

                militaries = models.Military.objects.filter(
                    self.build_filter_conditions(term)
                ).exclude(id=request.user.military.id)
                # page = self.paginate_queryset(queryset)
                # serializer = self.get_serializer(page, many=True) if page is not None else self.get_serializer(queryset, many=True)
                data = []
                for military in militaries:
                    if military.rank and military.nickname:
                        text = f"{military.register} ({military.rank} {military.nickname})"
                    else:
                        text = f"{military.register} ({military.name})"

                    data.append({
                        'id': military.pk,
                        'text': text
                    })
                return JsonResponse(data, safe=False)
                # return self.get_paginated_response(serializer.data)
        except Exception as e:
            logger.error('Error while getting military - {}'.format(e))
        
    def build_filter_conditions(self,term):
        logger.info('No filtro personalizado - {}'.format(self.request.user))
        filters = Q()
        try:
            # TODO atualizar parâmetros
            query_dict = {'name':  'name', 'cpf': 'cpf', 'nickname': 'nickname', 'register': 'register', 'email': 'email'}

            for field, flag in query_dict.items():
                if term:
                    q = Q(**{f"{flag}__icontains":term}) if field in ['cpf', 'register'] else Q(
                        **{f"{flag}__unaccent__icontains":term})
                    filters |= q
            logger.info('Query_filter - {}'.format(filters))
            return filters
        except Exception as e:
             logger.Error('Exception - {}'.format(e))
             raise e
         

class SearchMilitaryView(View):
    """
    Busca por Militares e retorna os resultados em uma lista HTML.
    """
    def get(self, request, action_type=None, *args, **kwargs):
        query = request.GET.get("search", "").strip()
        militaries = models.Military.objects.filter(
            Q(nickname__icontains=query) |
            Q(name__icontains=query) |
            Q(register__icontains=query) |
            Q(cpf__icontains=query)
        ).distinct() if query else models.Military.objects.none()

        try:
            # Passar 'action_type' ao contexto para uso no template
            html = render_to_string(
                "portal/partials/military_options.html",
                {"militaries": militaries, "action_type": action_type}
            )
        except Exception as e:
            logger.warning("[Portal - SearchMilitaryView] - Error in search militaries: %s", e)
            html = ""

        return HttpResponse(html)

class SearchEnjoyerView(View):
    """
    Busca por Enjoyers e retorna os resultados em uma lista HTML.
    """
    def get(self, request, action_type=None, *args, **kwargs):
        query = request.GET.get("search", "").strip()
        print("QUERY: ", query)
        enjoyers = models.Enjoyer.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        ).distinct() if query else models.Enjoyer.objects.none()

        try:
            # Passar 'action_type' ao contexto para uso no template
            html = render_to_string(
                "portal/partials/enjoyer_options.html",
                {"enjoyers": enjoyers, "action_type": action_type}
            )
        except Exception as e:
            logger.warning("[Portal - SearchEnjoyerView] - Error in search enjoyers: %s", e)
            html = ""

        return HttpResponse(html)


class SearchEntityView(View):
    """
    Busca por Entidades e retorna os resultados em uma lista HTML
    """
    def get(self, request, *args, **kwargs):
        query = request.GET.get("search", "").strip()
        if query:
            entities = models.Entity.objects.filter(
                Q(name__icontains=query)
            ).distinct()
        else:
            entities = models.Entity.objects.none()

        html = render_to_string(
            template_name="portal/partials/entity_options.html",
            context={"entities": entities}
        )
        return HttpResponse(html)
