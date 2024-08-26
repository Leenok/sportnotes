from django.contrib import admin
from django.urls import path

from training.views import competitions, add_competitions, add_discipline, setCompleted, main, all_events, add_event, delete_training_line, delete_basic_approach, add_training_line, add_basic_approach, add_new_plan, delete_new_plan, trainings, add_new_training, delete_new_training, setNotCompleted, show_training_plan, vue_test
from authorization.views import auth, out, reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('main/', main),
    # 404 not found
    path('vue_test', vue_test),

    path('auth/', auth),
    path('reg/', reg),
    path('out/', out),

    # event
    path('all_events/', all_events),
    path('add_event/', add_event, name="add_event"),
    
    # competition
    path('competitions_list/', competitions),
    path('add_competitions/', add_competitions),
    path('add_discipline/', add_discipline),
    
    # plan
    path('training_plans/', show_training_plan), 
    path('add_new_plan/', add_new_plan),
    path('delete_new_plan/', delete_new_plan),
    path('add_basic_approach/', add_basic_approach),
    path('delete_basic_approach/', delete_basic_approach),
    
    # training
    path('trainings/', trainings),
    path('add_new_training/', add_new_training),
    path('delete_new_training/', delete_new_training),
    path('add_training_line/', add_training_line),
    path('delete_training_line/', delete_training_line),
    path('setCompleted/', setCompleted),
    path('setNotCompleted/', setNotCompleted),
]
