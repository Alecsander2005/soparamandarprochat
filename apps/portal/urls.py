# apps/portal/urls.py
from django.urls import path

from apps.portal import views

app_name = 'portal'

urlpatterns = [
    path('api-v1/entity_list_json/', views.EntityListJson.as_view(), name='entity_list_json'),
    path('list_entity/', views.EntityListView.as_view(), name='list_entity'),
    path('command_portal/', views.ComandosAPIPortalView.as_view(), name='command_portal'),
    path('search-military/', views.SearchMilitaryView.as_view(), name='search_military'),
    path('militaries/', views.AutocompleteMilitaryView.as_view(), name='list_militaries'),
    # Get Partials
    path('search-military/', views.SearchMilitaryView.as_view(), name='search_military'),
    path('search-military/<str:action_type>/', views.SearchMilitaryView.as_view(), name='search_military_with_type'),
    path('search-entity/', views.SearchEntityView.as_view(), name='search_entity'),
    path('search-enjoyer/', views.SearchEnjoyerView.as_view(), name='search_enjoyer'),
    path('search-enjoyer/<str:action_type>/', views.SearchEnjoyerView.as_view(), name='search_enjoyer_with_type'),
]

