from django.urls import path
from events.views import event,dashboard,create_event

urlpatterns = [
    path('event/', event),
    path('dashboard/', dashboard),
    path('create-event/', create_event, name='create-event'),
]