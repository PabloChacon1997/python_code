from django.http import JsonResponse
import requests
import base64
import json
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt
import pyrebase
from datetime import date
# Create your views here.


@csrf_exempt
def subirImagen(request):
    firebaseConfig = {
        'apiKey': "AIzaSyBRWvbJvMjs4J_hPUsTKaPQKt7-ISK3T2o",
        'authDomain': "pythonfirebase-f55ac.firebaseapp.com",
        'databaseURL': "https://pythonfirebase-f55ac.firebaseio.com",
        'projectId': "pythonfirebase-f55ac",
        'storageBucket': "pythonfirebase-f55ac.appspot.com",
        'messagingSenderId': "1012266754514",
        'appId': "1:1012266754514:web:b40da7bfc04cbcbf87280b"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)

    if request.method == 'POST':
        img = request.FILES['imagen']
        body = request.POST.get('usuario')
        men = request.POST.get('mensaje')
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
        hoy = date.today()
        resjson = res.json()
        res1 = json.dumps(resjson)
        res3 = json.loads(res1)
        urlbucket = res3['url']
        print(urlbucket , hoy)
        d1 = hoy.strftime("%d/%m/%Y")
        firebaseRes = requests.post('https://pythonfirebase-f55ac.firebaseio.com/datos.json',
        json=json.dumps({
            'fecha': d1,
            'mensaje': men,
            'url': urlbucket,
            'usuario': body
            })
        )
        return JsonResponse(firebaseRes.json())
    if request.method == 'GET':
        res2 = requests.get('https://pythonfirebase-f55ac.firebaseio.com/datos.json')
        return JsonResponse(res2.json())


    return JsonResponse({
        'status': 400,
        'message': 'ERROR: Hacer un GET o POST'
    })

