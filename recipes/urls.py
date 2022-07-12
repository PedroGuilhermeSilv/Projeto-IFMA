from django.urls import path

from . import views

urlpatterns = [
    path('',views.recipe),
    # path('',views.home),
    # path('recipes/<int:id>/',views.recipe),
    path('menu/',views.menu),
    path('cadastro/',views.cadastro),

]
