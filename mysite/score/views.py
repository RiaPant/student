from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, reverse
from .models import Person
from .forms import Personform


def index(request):
    # ppl=Person.objects.order_by('marks')
    return render(request, 'score/index.html', {})


def results(request):
    ppl = Person.objects.order_by('marks')
    return render(request, 'score/results.html', {'ppl': ppl})


def create(request):
    if request.method == 'POST':
        form = Personform(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            enroll_no = request.POST.get('enroll_no', '')
            marks = request.POST.get('marks', '')
            person = Person(first_name=first_name, last_name=last_name, enroll_no=enroll_no, marks=marks)
            person.save()

            return HttpResponseRedirect(reverse('score:create'))
    else:
        form = Personform()

    return render(request, 'score/create.html', {
        'form': form
        }

                      )

# create a dictionary to print
