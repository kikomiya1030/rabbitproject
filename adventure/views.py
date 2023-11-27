from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import PyTest

import random

# Create your views here.

class AdventureView(TemplateView):
    template_name = 'adventure.html'

class QuestionView(TemplateView):
    template_name = 'question.html'

    def get_context_data(self, **kwargs):
        random_count = PyTest.objects.count() # データベース存在しているデータ確認
        randomid = random.randint(1, random_count-1) # データベースに存在している数字をランダムに出す

        random_index = PyTest.objects.all()[randomid] # ランダムした番号のすべてのデータを取り出す
        kwargs['random_index'] = random_index
        return super().get_context_data(**kwargs)

class AnswerView(TemplateView):
    template_name = 'answer.html'

    def get_context_data(self, **kwargs):
        record_id = self.request.GET.get('record_id') # htmlからデータベース対応するid番号を受け取り
        record_id = int(record_id)

        record = PyTest.objects.get(id=record_id)
        kwargs['record'] = record

        return super().get_context_data(**kwargs)