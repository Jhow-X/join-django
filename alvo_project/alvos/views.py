from django.shortcuts import render, get_object_or_404
from .models import Alvo
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
import json


def index(request):
    alvos = Alvo.objects.all()
    return render(request, 'alvos/index.html', {'alvos': alvos})

@csrf_exempt
def api_alvos(request, id=None):
    if request.method == 'GET':
        # Caso de listar todos os alvos
        alvos = Alvo.objects.all()
        data = [{"id": alvo.id, "nome": alvo.nome, "latitude": alvo.latitude, "longitude": alvo.longitude} for alvo in alvos]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        # Caso de criar um novo alvo
        try:
            data = json.loads(request.body)
            alvo = Alvo.objects.create(
                nome=data['nome'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                identificador=data.get('identificador', ''),
                data_expiracao=data.get('data_expiracao', None)
            )
            return JsonResponse({"id": alvo.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    elif request.method == 'PUT' and id:
        # Caso de editar um alvo existente
        try:
            alvo = Alvo.objects.get(id=id)
            data = json.loads(request.body)
            alvo.nome = data.get('nome', alvo.nome)
            alvo.latitude = data.get('latitude', alvo.latitude)
            alvo.longitude = data.get('longitude', alvo.longitude)
            alvo.identificador = data.get('identificador', alvo.identificador)
            alvo.data_expiracao = data.get('data_expiracao', alvo.data_expiracao)
            alvo.save()
            return JsonResponse({"id": alvo.id})
        except Alvo.DoesNotExist:
            return JsonResponse({"error": "Alvo not found"}, status=404)

    elif request.method == 'DELETE' and id:
        # Caso de excluir um alvo
        try:
            alvo = Alvo.objects.get(id=id)
            alvo.delete()
            return JsonResponse({"message": "Alvo deleted successfully"})
        except Alvo.DoesNotExist:
            return JsonResponse({"error": "Alvo not found"}, status=404)
    
    else:
        return HttpResponseNotAllowed(["GET", "POST", "PUT", "DELETE"])