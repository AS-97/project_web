from django.shortcuts import render
from .models import LiveText, LiveImage
from django.http import JsonResponse


def hello_world(request):
    return render(request, 'hello.html')

#def home(request):
#    text = LiveText.objects.first()  # Načte první text z databáze
#    return render(request, 'home.html', {'text': text})

def get_text(request):
    text = LiveText.objects.first()  # Načte první text z databáze
    return JsonResponse({'content': text.content})

# View pro načtení stránky
def home(request):
    image = LiveImage.objects.first()  # Načte první obrázek z databáze
    return render(request, 'home.html', {'image': image})

# API endpoint pro získání obrázku
def get_image(request):
    image = LiveImage.objects.first()
    if image:
        return JsonResponse({'image_url': image.image.url})
    return JsonResponse({'error': 'Obrázek nebyl nalezen'}, status=404)