from django.http import JsonResponse
import requests
import base64
import json
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def subirImagen(request):
    if request.method == 'POST':
        img = request.FILES['imagen']
        imagen_str = base64.b64encode(img.read()).decode('utf-8')
        ext = img.content_type.replace('image/', '.')
        print(imagen_str)
        res = requests.post(
            'https://amm0154z9d.execute-api.us-east-1.amazonaws.com/test1',
            json=json.dumps({
                'imagen': imagen_str,
                'nombre': f'{uuid4()}{ext}'
            })
        )
        return JsonResponse(res.json())

    return JsonResponse({
        'status': 400,
        'message': 'ERROR: Solo se aceptan peticiones POST'
    })

