from django.urls import path
from.import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('peliculas/agregar', views.agregar, name='agregar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('peliculas/editar/<int:id>/', views.editar, name='editar')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)