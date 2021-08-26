from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .forms import PersonForm
from .models import Person


def people_fn(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Спасибо, новый пользователь создан!')
    data = {'form': form}
    return render(request, 'people.html', context=data)


def person_id(request, p_id):
    obj = get_object_or_404(Person, pk=p_id)
    form = PersonForm(instance=obj)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные сохранены')
    data = {'form': form}
    return render(request, 'people.html', context=data)
