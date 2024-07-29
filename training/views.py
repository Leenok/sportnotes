from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Competition, Discipline, Exercise, Program, Training, Approach
from .forms import CompetitionForm, DisciplineForm
import calendar
from datetime import datetime

def index(request):
    # exc = Exercise.objects.all()
    # print(exc)
    pr = Program.objects.all()
    print(pr)
    apr =Approach.objects.all()
    print(apr)
    pr.delete()
    # exc.delete()
    apr.delete()
    return render(request, "main.html")

def showTrainings(request):
    user_id = request.user.id
    list_trainings = Training.objects.filter(sportsmen = user_id)
    list_program = Program.objects.all
    exc_for_trainings = {}
    for i in list_trainings:
        exc_for_trainings[i.programm_name] = Program.objects.filter(name = i.programm_name)

    print(list_program)
    return render(request, "training/training.html", {'list_trainings':list_trainings, 'list_program':list_program})


def competitions(request):
    c = calendar.HTMLCalendar()
    html_out1 = c.formatmonth(datetime.today().year, datetime.today().month-1)
    html_out = c.formatmonth(datetime.today().year, datetime.today().month)
    html_out2 = c.formatmonth(datetime.today().year, datetime.today().month+1)
    
    user_id = request.user.id
    list_competitions = Competition.objects.filter(sportsmen = user_id)
    name = request.user.username
    return render(request, "training/competitions.html", {'list_competitions':list_competitions, 'name':name, 'html_out':html_out, 'html_out2':html_out2, 'html_out1':html_out1})

def add_competitions(request):
    error = ''
    sportsmen = request.user
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():     
            newcompetitions = form.save(commit=False)
            newcompetitions.sportsmen = sportsmen
            newcompetitions.save()
            return redirect(competitions)
        else:
            error = form.errors

    form = CompetitionForm()

    data ={
        'form': form,
        'error': error
    }
    return render(request, "training/add_competitions.html", data)

def edit_competitions(request):
    # Create a form to edit an existing Article, but use
    # POST data to populate the form.
    # a = Article.objects.get(pk=1)
    # f = ArticleForm(request.POST, instance=a)
    # f.save()
    pass

def add_discipline(request):
    error = ''
    if request.method == "POST":
        form = DisciplineForm(request.POST)
        if form.is_valid():
            newDisc = form.save()
            print(newDisc)
            return redirect(index)
        else:
            error = 'Форма не верная'
    
    form = DisciplineForm()
    data2 ={
        'form': form,
        'error': error
    }
    return render(request, "training/add_discipline.html", data2)