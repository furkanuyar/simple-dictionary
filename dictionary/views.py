from django.shortcuts import render
from .models import Word
from .forms import DictionaryForm


def dictionary(request):
    words = []
    cond = False
    if request.method == "POST":
        form = DictionaryForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['name']
            words = Word.objects.filter(name=word.lower())
            cond = bool(words)
    form = DictionaryForm()
    return render(request, 'dictionary/dictionary.html', {'form': form,
                                                          'words': words,
                                                          'cond': cond,
                                                          'method': request.method})
