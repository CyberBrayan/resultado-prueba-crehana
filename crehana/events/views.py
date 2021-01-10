from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from rest_framework.views import APIView
from crehana.gestion.models import Inscription
from crehana.events.tasks import create_event
from django.core.exceptions import ObjectDoesNotExist

def validate_fields(data):
    fields = {}

    if not ('event_type' in data):
        fields["event_type"] = ["This field is required."]
    
    if not ('minute' in data):
        fields["minute"] = ["This field is required."]

    if not ('inscription' in data):
        fields["inscription"] = ["This field is required."]
    
    return fields

def validate_number_field(data):
    return type(data["event_type"]).__name__ == "int" and type(data["minute"]).__name__ == "int" and type(data["inscription"]).__name__ == "int"

def validate_event(event_type):
    switcher = {
        1: "Inicio de video",
        2: "Pausa",
        3: "Reproducción",
        4: "Final del video"
    }
    return switcher.get(event_type, "El evento no existe")

class EventAPIView(APIView):
    authentication_classes = [SessionAuthentication,
        BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        result = validate_fields(request.data)
        if len(result) == 0:
            if(validate_number_field(request.data)):
                try:
                    inscription = Inscription.objects.get(id=request.data["inscription"])
                except ObjectDoesNotExist:
                    inscription = None

                if not inscription:
                    response = JsonResponse({'mensaje': 'La inscripción no existe'}, status = 404)
                else:
                    if validate_event(request.data["event_type"]) != "El evento no existe":
                        create_event.delay(request.data)
                            
                        response = JsonResponse({'mensaje': 'Operación exitosa'}, status = 201)
                    else:
                        response = JsonResponse({'mensaje': 'El evento no existe'}, status = 404)
            else:
                response = JsonResponse({'mensaje': 'Los valores deben ser numéricos'}, status = 400)
        else:
            response = JsonResponse(result, status = 400)
        
        return response
       
