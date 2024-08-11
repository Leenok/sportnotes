from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from swingtime.models import Event
from .models import Competition, Discipline, Exercise, Program, Training, Approach
from .forms import CompetitionForm, DisciplineForm, ApproachForm, TrainingForm, ProgramForm
import calendar
from datetime import datetime

def main(request):
    all_events = Training.objects.all()
    context = {
        "events": all_events,
    }
    return render(request, "main.html", context)
        
def all_events(request):
    all_events = Training.objects.all()
    out = []
    for training in all_events:
        out.append({
            'title': training.name,
            'id': training.id,
            'start': training.date.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': training.date.strftime("%m/%d/%Y, %H:%M:%S")
        })
    return JsonResponse(out, safe=False)

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Training(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)

def sport_events(request):
    events = Event.objects.all()
    return render(request,"events.html", {'events':events})

# training plan
def show_training_plan(reguest):
    form = ProgramForm()
    list_program = Program.objects.all()
    list_plan_name = []
    for i in list_program:
        if i.name not in list_plan_name:
            list_plan_name.append(i.name)
    data = {
        'list_program':list_program,
        'list_plan_name': list_plan_name,
        'form': form
    }
    return render(reguest, "training/training_plans.html", data)

def add_training_plan(request):
    error = ''
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():     
            form.save()
            return redirect(show_training_plan)
        else:
            error = form.errors

    data ={
        'form': form,
        'error': error
    }
    return render(request, "training/training_plans.html", data)


def delete_plan(request):
    plan_name = request.POST.get("plan_name")
    Program.objects.filter(name=plan_name).delete()
    return redirect(show_training_plan)

def delete_exercise_from_program(request):
    program_id = request.POST.get("id_plan_exercise")
    Program.objects.get(id=int(program_id)).delete()
    return redirect(show_training_plan)

def add_exercise_to_plan(request):
    # error = ''
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        print(form.is_valid())
        form.save()
        return redirect(show_training_plan)
    # else:
    #     error = form.errors
    return redirect(show_training_plan)

# training
def showTrainings(request):
    user_id = request.user.id
    list_trainings = Training.objects.filter(sportsmen = user_id).order_by('-date')
    list_program = Program.objects.all()
    exc_for_trainings = {}
    list_approach = Approach.objects.all()
    for i in list_trainings:
        exc_for_trainings[i.programm_name] = Program.objects.filter(name = i.programm_name)
        # list_approach.push(Approach.objects.filter(training_id=i.id))

    form = ApproachForm()

    data ={
        'list_trainings':list_trainings,
        'list_program':list_program,
        'list_approach':list_approach,
        'form': form
    }
    return render(request, "training/training.html", data)

def add_training(request):
    list_program = Program.objects.all()
    list_program_names = []
    for i in list_program:
        if i.name not in list_program_names:
            list_program_names.append(i.name)
    error = ''
    sportsmen = request.user
    if request.method == "POST":
        form = TrainingForm(request.POST)      
        if form.is_valid():
            newTrn = form.save(commit=False)
            newTrn.sportsmen = sportsmen
            newTrn = form.save()
            program_training = Program.objects.filter(name = newTrn.programm_name)
            nTrn = Training.objects.get(id=newTrn.id)
            for execise in program_training:
                for i in range(execise.count_approach):	
                    tom = Approach.objects.create(training_id=nTrn, programm_id=execise, number=i+1, isCompleted=False, quantity=execise.repeat, weight=50, time=2, time_rest=1)
                    print(f'new appr {i} {tom}')
            return redirect(showTrainings)
        else:
            form.errors
    form = TrainingForm()

    data ={
        'form': form,
        'error': error,
        'list_program_names': list_program_names
    }
    return render(request, "training/add_training.html", data)

def delete_training(request):
    training_id = request.POST.get("training_id")
    Training.objects.get(id=int(training_id)).delete()
    return redirect(showTrainings)


# approache
def add_approach(request):
    error = ''
    if request.method == "POST":
        form = ApproachForm(request.POST)      
        if form.is_valid():
            form.save()
            return redirect(showTrainings)
        else:
            form.errors
    form = ApproachForm()
    data ={
        'form': form,
        'error': error
    }
    return render(request, "training/training.html", data)

def setCompleted(request):
    approach_id = request.POST.get("approach_id")
    approach = Approach.objects.get(id=int(approach_id))
    approach.isCompleted = True
    approach.save(update_fields=['isCompleted'])
    return redirect(showTrainings)

# competitions
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

# discipline
def add_discipline(request):
    error = ''
    if request.method == "POST":
        form = DisciplineForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "main.html")
        else:
            error = form.errors
    
    form = DisciplineForm()
    data2 ={
        'form': form,
        'error': error
    }
    return render(request, "training/add_discipline.html", data2)

