from django.db import models

class Articulos(models.Model):
    
    codigo=models.CharField(max_length=7)
    nombre=models.CharField(max_length=30) 
    seccion=models.CharField(max_length=20) 
    precio=models.IntegerField() 
    imagen=models.ImageField(upload_to="productos")
    
    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

class Meta:
    verbose_name = "articulo"
    verbose_name_plural = "articulos"


    def __str__(self):
        return f"El articulo: {self.nombre}, con codigo {self.codigo} pertenece a la seccion {self.seccion} y tiene un precio de {self.precio}"

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
