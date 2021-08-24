from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonForm


def people(request):
    form = PersonForm()
    data = {'form': form}
    return render(request, 'people.html', context=data)
