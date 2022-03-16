from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
    path('cross_off/<todo_id>/', views.cross_off, name="cross_off"),
    path('uncross/<todo_id>/', views.uncross, name="uncross"),
    path('dlt_completed', views.dlt_completed, name="dlt_completed"),
]
