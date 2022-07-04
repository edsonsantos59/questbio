from django.contrib import admin
from django.urls import path
from projeto5_website import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),
    path('obrigado/<int:id>/<int:cpf>/<str:instituicao>', views.obrigado, name="obrigado"),
    path('test/<str:teste>', views.test, name="test"),
    path('logout/', views.logout_user, name='logout'),
    path('resultado/admin/c5052cf355e48dc43b7a21bfc38e2dd1/', views.resultado, name='resultado'),
]