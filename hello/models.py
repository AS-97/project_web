from django.db import models

class LiveText(models.Model):
    content = models.CharField(max_length=255)  # Text, který se zobrazí na stránce

    def __str__(self):
        return self.content
    
class LiveImage(models.Model):
    image = models.ImageField(upload_to='images/')  # Uložení cesty k obrázku

    def __str__(self):
        return f"Obrázek: {self.image.name}"
