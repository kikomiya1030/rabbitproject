from django.urls import path
from . import views
app_name = 'adventure'

urlpatterns = [
    path('adventure/',views.AdventureView.as_view(), name='adventure'),
    path('question/', views.QuestionView.as_view(), name='question'),
    path('answer/', views.AnswerView.as_view(), name='answer'),
]
