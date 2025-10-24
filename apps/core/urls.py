from .views import IndexView, LoginView, LogoutView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('exemplo/', include('apps.exemplo.urls'), name="exemplo"),
    path('imagem/', include('apps.imagem.urls'), name="imagem"),
    path('criminoso/', include('apps.criminoso.urls'), name="criminoso"),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
