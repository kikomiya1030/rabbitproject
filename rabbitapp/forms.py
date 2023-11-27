from django import forms
from django.forms import ModelForm
from .models import RabbitPost

class ContactForm(forms.Form):
    name = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
            'Please input your name.'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = \
            'Please input your email address.'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = \
            'Please input the title about your question.'
        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = \
            'Please advise the content about your problem.'
        self.fields['message'].widget.attrs['class'] = 'form-control'

class RabbitPostForm(ModelForm):
    class Meta:
        ModelForm = RabbitPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']