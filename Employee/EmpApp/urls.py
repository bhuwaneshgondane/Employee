from django.urls import path
from .views import addView, showView, updateView, deleteView

urlpatterns = [
    path('add/', addView, name='add'),
    path('show/', showView, name='show'),
    path('update/<int:pk>/', updateView, name='update'),
    path('delete/<int:pk>/', deleteView, name='delete'),
]
