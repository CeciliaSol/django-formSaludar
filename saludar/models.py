from django.db import models

class Tarea(models.Model):
    tarea = models.CharField(max_length=50)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.tarea


