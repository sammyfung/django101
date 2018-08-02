from django.urls import path
from . import views

# new path() is used in latest django 2.x
urlpatterns = [
    path('api/add_participant/<int:event_id>', views.api_add_participant, name="api_add_participant"),
    path('participant/<int:participant_id>', views.view_participant, name="view_participant"),
    path('<int:event_id>/add', views.add_participant, name="add_participant"),
    path('<int:event_id>', views.list_participant, name="list_participant"),
    path('', views.list_event, name='list_event'),
]
