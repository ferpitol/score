from django.urls import path
from API.views_score import Scores as Scores_view

urlpatterns = [
    path('api/scores', Scores_view.as_view(), name='score'),
]