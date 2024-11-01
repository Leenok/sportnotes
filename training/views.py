from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
# from swingtime import Event
from .models import Competition, Discipline, Exercise, Program, Training, Approach, TrainingPlan, TrainingLine, BasicApproach, NewTraining, NewTrainingLine, NewApproach
from .forms import CompetitionForm, DisciplineForm, ApproachForm, NewTrainingForm, TrainingForm, ProgramForm, TrainingLineForm, BasicApproachForm, TrainingPlanForm, NewApproachForm
import calendar
from datetime import datetime

# vue
def vue_test(request):
    return render(request, "training/vue.html")


# training plan
def show_training_plan(reguest):
    # new
    training_plans = TrainingPlan.objects.all()
    training_lines = TrainingLine.objects.all()
    basic_approaches_all = BasicApproach.objects.all()
    trainingPlanForm = TrainingPlanForm()
    formTrainingLine = TrainingLineForm()
    formBasicApproach = BasicApproachForm()
    list_type_of_approachs = ['quantity', 'waight_and_quantity', 'distance', 'time', 'temp_and_distance']
    
    # old
    form = ProgramForm()
    list_program = Program.objects.all()
    list_plan_name = []
    for i in list_program:
        if i.name not in list_plan_name:
            list_plan_name.append(i.name)
    data = {
        'list_program':list_program,
        'list_plan_name': list_plan_name,
        'form': form,
        'training_plans': training_plans,
        'training_lines': training_lines,
        'basic_approaches_all': basic_approaches_all,
        'list_type_of_approachs': list_type_of_approachs,
        'formTrainingLine': formTrainingLine,
        'formBasicApproach': formBasicApproach,
        'trainingPlanForm': trainingPlanForm,
    }
    return render(reguest, "training/training_plans.html", data)

# new plan
def add_new_plan(request):
    error = ''
    sportsmen = request.user
    if request.method == "POST":
        if(request.POST.get("name") == ''):
            return redirect(show_training_plan)
        form = TrainingPlanForm(request.POST)

        if form.is_valid():
            new_plan = form.save(commit=False)
            new_plan.sportsmen_id = sportsmen
            new_plan = form.save()
            return redirect(show_training_plan)
        else:
            form.errors
    data ={
        'form': form,
        'error': error
        }
    return render(request, "training/training_plans.html", data)

def delete_new_plan(request):
    id = request.POST.get("id")
    TrainingPlan.objects.get(id=id).delete()
    return redirect(show_training_plan)

def add_training_line(request):
    error = ''
    if request.method == 'POST':
        print(request.POST.get("type_of_approaches"))
        form = TrainingLineForm(request.POST)
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

def delete_training_line(request):
    training_line_id = request.POST.get("id")
    TrainingLine.objects.get(id=training_line_id).delete()
    return redirect(show_training_plan)

def add_basic_approach(request):
    error = ''
    if request.method == "POST":
        form = BasicApproachForm(request.POST)      
        if form.is_valid():
            new_approach= form.save(commit=False)
            number = len(BasicApproach.objects.filter(training_line_id=int(request.POST.get("training_line_id"))))
            print(number)
            new_approach.number = number+1
            new_approach.save()
            return redirect(show_training_plan)
        else:
            error = form.errors
    data ={
        'form': form,
        'error': error
        }
    return render(request, "training/training_plans.html", data)

def delete_basic_approach(request):
    basic_approach_id = request.POST.get("id")
    BasicApproach.objects.get(id=basic_approach_id).delete()
    return redirect(show_training_plan) 
 

# new show/add trainig 
def trainings(request):
        # new
    new_training_list = NewTraining.objects.all().order_by('-training_date').values()
    new_training_lines = NewTrainingLine.objects.all()
    new_approaches_all = NewApproach.objects.all()
    form_new_training = NewTrainingForm()
    form_to_approah = NewApproachForm()
    data = {
        'new_training_list': new_training_list,
        'new_training_lines': new_training_lines,
        'new_approaches_all': new_approaches_all,
        'form_new_training': form_new_training,
        'form_to_approah': form_to_approah,
    }
    return render(request, "training/all_trainings.html", data)

def add_new_training(request):
    error = ''
    sportsmen = request.user
    if request.method == "POST":
        form = NewTrainingForm(request.POST)      
        if form.is_valid():
            new_training = form.save(commit=False)
            new_training.sportsmen_id = sportsmen
            new_training.save()
            createLineandSetsForTraining(new_training, new_training.training_plan_id)
            return redirect(trainings)
        else:
            form.errors
    form = NewTrainingForm()
    data ={
        'form': form,
        'error': error
    }
    return render(request, "training/all_trainings.html", data)

def createLineandSetsForTraining(training, plan):
    lines = TrainingLine.objects.filter(training_plan_id=plan)
    for line in lines:
        # create line to training 
        new_line = NewTrainingLine.objects.create(
            training_id=training,
            exercise_id=line.exercise_id,
            type_of_approaches=line.type_of_approaches
            )
        sets = BasicApproach.objects.filter(training_line_id = line)
        # create sets copy from plan waight and time 
        for set in sets:
            new_set = NewApproach.objects.create(
                line_id=new_line,
                number=set.number,
                quantity=set.quantity,
                weight=set.weight,
                distance=set.distance,
                type_temp=set.type_temp,
                time=set.time,
                time_rest=set.time_rest,
                isCompleted=False,
            )
            print(new_set.number)

def setCompleted(request):
    approach_id = request.POST.get("set")
    approach = NewApproach.objects.get(id=int(approach_id))
    approach.isCompleted = True
    approach.save(update_fields=['isCompleted'])
    return redirect(trainings)

def setNotCompleted(request):
    approach_id = request.POST.get("set")
    approach = NewApproach.objects.get(id=int(approach_id))
    approach.isCompleted = False
    approach.save(update_fields=['isCompleted'])
    return redirect(trainings)

def delete_new_training(request):
    training_id = request.POST.get("id")
    NewTraining.objects.get(id=training_id).delete()
    return redirect(trainings)

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

# events 
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

# def sport_events(request):
#     events = Event.objects.all()
#     return render(request,"events.html", {'events':events})

