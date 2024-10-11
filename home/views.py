
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import VisitCounter


def home_view(request: HttpRequest) -> HttpResponse:
    visit_counter, created = VisitCounter.objects.get_or_create(id=1)
    visit_counter.visits += 1
    visit_counter.save()
    return render(request, 'main/index.html')

def monitoring_view(request: HttpRequest) -> HttpResponse:
    visit_counter = VisitCounter.objects.get(id=1)

    return render(request, 'monitoring/index.html', {'visits': visit_counter.visits})



