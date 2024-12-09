from django.db import models

# Create your models here.

class Kid(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SecretSantaAssignment(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    secret_santa = models.ForeignKey(Kid, related_name='assigned_kid', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.kid.name} -> {self.secret_santa.name}'

