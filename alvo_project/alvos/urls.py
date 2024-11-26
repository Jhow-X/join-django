from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial
    path('api/alvos/', views.api_alvos),  # API para listar/criar alvos
    path('api/alvos/<int:id>/', views.api_alvos),  # API para editar/excluir alvos (com ID)
]

# # alvos/urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import AlvoViewSet
# from . import views


# router = DefaultRouter()
# router.register(r'alvos', AlvoViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('', views.index, name='index')
# ]

