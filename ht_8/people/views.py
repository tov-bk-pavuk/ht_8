from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PersonForm
from .models import Person


def people_fn(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse(f'Спасибо, новый пользователь создан!')
    data = {'form': form}
    return render(request, 'people.html', context=data)


def person_id(request, id):
    obj = get_object_or_404(Person, pk=id)
    return HttpResponse(f'{obj}')

def person_ed(request, id):
    a = Person.objects.get(pk=id)
    f = PersonForm(request.POST, instance=a)
    if f.is_valid():
        f.save()
