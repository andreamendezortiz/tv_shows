from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 4:
            errors["title"] = "El nombre del programa debe tener más de 4 caracteres"
        if len(postData['description']) < 8:
            errors["description"] = "La descripción del programa debe tener más de 8 caracteres"
        return errors

class Network(models.Model):
    name = models.CharField(max_length=455)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Show(models.Model):
    network = models.ForeignKey(Network, related_name="shows", on_delete= models.CASCADE)
    title = models.CharField(max_length=455)
    description = models.CharField(max_length=455)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self) -> str:
        return f'{self.id}{self.title}'





