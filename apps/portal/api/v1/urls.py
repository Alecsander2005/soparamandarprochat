from django.urls import path

from apps.portal.api.v1 import viewsets

app_name = 'apps.portal'

urlpatterns = [
    path('militaries/', viewsets.MilitaryListView.as_view(), name='list_militaries'),
    path('militaries/image/<str:username>/', viewsets.MilitaryImageView.as_view(), name='image_militaries'),
]