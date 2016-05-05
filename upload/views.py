from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from view.models import post_jianzhi
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .forms import ExamInfoForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExamInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return render(request, 'tiuzyun.html')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExamInfoForm()
    return render(request, 'upload.html', {'form': form})
