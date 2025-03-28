from django.shortcuts import render,redirect
from events.forms import EventForm
from .models import Event, Participant, Category
from django.db.models import Count, Q

def event(request):
    events = Event.objects.select_related("category").prefetch_related("participants")
    return render(request, "event.html", {"events": events})

def dashboard(request):
    
    events = Event.objects.annotate(count=Count('participants'))
    
    from django.utils.timezone import datetime
    today = datetime.today()
    counts = Event.objects.aggregate(
        total_events=Count('id'),
        total_participants=Count('participants', distinct=True),
        upcoming_events=Count('id', filter=Q(date__gte=today)),
        past_events=Count('id', filter=Q(date__lt=today))
    )
    
    context={
        "events":events,
        "counts":counts
    }
    
    return render(request, "dashboard.html", context)

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('create-event')
    else:
        form = EventForm()
    
    return render(request, 'form.html', {'form': form})