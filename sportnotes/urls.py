from django.contrib import admin
from django.urls import path

from training.views import competitions, add_competitions, add_discipline, showTrainings, add_training, delete_training, add_approach, setCompleted, show_training_plan, main, all_events, add_event, add_training_plan, delete_exercise_from_program, delete_plan, add_exercise_to_plan, delete_training_line, delete_basic_approach, add_training_line, add_basic_approach, add_new_plan, delete_new_plan, trainings, add_new_training, del_new_training
from authorization.views import auth, out, reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('main/', main),

    path('auth/', auth),
    path('reg/', reg),
    path('out/', out),

    path('all_events/', all_events),
    path('add_event/', add_event, name="add_event"),
    
    path('competitions_list/', competitions),
    path('add_competitions/', add_competitions),

    path('add_discipline/', add_discipline),

    path('training/', showTrainings),
    path('add_training/', add_training),

    path('training/delete_training/', delete_training),
    path('training/add_approach/', add_approach),
    path('training/setCompleted/', setCompleted),

    path('training_plans/', show_training_plan),
    path('training_plans/add_training_plan/', add_training_plan),
    path('delete_exercise_from_program/', delete_exercise_from_program),
    path('add_exercise_to_plan/', add_exercise_to_plan),
    path('delete_plan/', delete_plan),
    
    
    path('add_new_plan/', add_new_plan),
    path('delete_new_plan/', delete_new_plan),

    path('add_training_line/', add_training_line),
    path('delete_training_line/', delete_training_line),
    
    path('add_basic_approach/', add_basic_approach),
    path('delete_basic_approach/', delete_basic_approach),

    path('trainings/', trainings),
    path('add_new_training/', add_new_training),
    path('del_new_training/', del_new_training),

]
