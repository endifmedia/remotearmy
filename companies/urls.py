from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<int:company_id>/', views.company)
]