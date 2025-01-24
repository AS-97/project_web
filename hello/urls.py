from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('home/', views.home, name='home'),  # Zobrazení stránky
    path('api/text/', views.get_text, name='get_text'),  # API endpoint
    path('api/image/', views.get_image, name='get_image'),  # API endpoint pro obrázek
]