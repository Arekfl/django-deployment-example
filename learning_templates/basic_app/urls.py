from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('other', views.other1, name='other2'),
    path('relative', views.relative, name='relative'),
]
