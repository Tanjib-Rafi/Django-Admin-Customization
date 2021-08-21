from django.db import models

class random(models.Model):
    name  = models.CharField(max_length=50)
    address = models.TextField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add=True)
    font_size = models.IntegerField()
    GENDER_CHOICES = [
   ('Male', 'Male'),
   ('Female', 'Female')
    ]
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    image = models.ImageField(null=True, blank=True)

def __str__(self):
    return self.name

def body_preview(self):
        return self.name
