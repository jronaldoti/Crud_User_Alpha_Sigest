from django.urls import path
from django.contrib.auth.urls import views as auth_views
from .views import UsuarioList, UsuarioDetail, UsuarioCreate,  UsuarioUpdate, UsuarioDelete

urlpatterns = [
    path('listar_usuario/', UsuarioList.as_view(), name='listar_usuario'),
    path('detalhar_usuario/<int:pk>/', UsuarioDetail.as_view(), name='detalhar_usuario'),
    path('cadastrar_usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('atualizar_usuario/<int:pk>/', UsuarioUpdate.as_view(), name='atualizar_usuario'),
    path('deletar_usuario/<int:pk>/', UsuarioDelete.as_view(), name='deletar_usuario'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
