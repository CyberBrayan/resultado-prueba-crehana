from celery import shared_task
from crehana.events.models import Event
from crehana.gestion.models import Inscription

@shared_task
def create_event(event):
    inscription = Inscription.objects.get(id=event["inscription"])
    
    Event.objects.create(
        event_type=event["event_type"],
        minute=event["minute"],
        inscription= inscription)