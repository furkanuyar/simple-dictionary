from django.forms import ModelForm
from .models import Word
from django import forms


class DictionaryForm(ModelForm):
    class Meta:
        model = Word
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Please type a word to search...'})
        }
        labels = {
            'name': 'Word'
        }
