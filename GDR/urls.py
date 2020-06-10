from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Accueil AKA Team Remplacements
    path('', views.index, name='index'),

    # Login/Logout system
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),

    # Ajout Remplacement
    path('my_replacements', views.my_replacements, name='my_replacements'),
    path('add/replacement', views.add_replacement, name='add_replacement'),
    path('add/reinstall', views.add_reinstall, name='add_reinstall'),
    path('add/install', views.add_install, name='add_install'),
    path('add/student_pc', views.add_student_pc, name='add_student_pc'),

    # Modification/Suppression Remplacement
    path('edit/<slug:type_p>/<slug:id_p>/', views.edit, name='edit'),
    path('delete/<slug:type_p>/<slug:id_p>/', views.delete, name='delete'),
]
