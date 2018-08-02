from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Event, Participant

# Create your views here.


def list_event(request):
    events = Event.objects.all()
    # pass a dictionary to render()
    data = { 'events': events }
    return render(request, 'eventmgr/events.html', data)


def list_participant(request, event_id):
    event = Event.objects.get(id=event_id)
    participants = Participant.objects.filter(event__id=event_id)
    data = { 'event': event, 'participants': participants }
    return render(request, 'eventmgr/participants_list.html', data)


def view_participant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    data = { 'participant': participant }
    return render(request, 'eventmgr/participants_view.html', data)


def add_participant(request, event_id):
    event = Event.objects.get(id=event_id)
    data = { 'event': event }
    return render(request, 'eventmgr/participants_add.html', data)


def api_add_participant(request, event_id):
    event = Event.objects.get(id=event_id)
    participant = Participant(event=event)
    participant.code = request.POST.get('code', '')
    participant.first_name = request.POST.get('first_name', '')
    participant.last_name = request.POST.get('last_name', '')
    participant.company = request.POST.get('company', '')
    participant.email = request.POST.get('email', '')
    participant.phone = request.POST.get('phone', '')
    participant.save()
    return HttpResponseRedirect(reverse('list_participant', kwargs={'event_id': event_id}))