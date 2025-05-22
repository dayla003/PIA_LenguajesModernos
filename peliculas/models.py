from django.db import models

# Create your models here.

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    sipnosis = models.TextField(verbose_name="Sipnosis", null=True)
    genero = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    opinion = models.TextField(verbose_name="Opinion", null=True, blank=True)

    def __str__(self):
        fila = " " + self.titulo + " - " + " " + self.genero
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()






    

