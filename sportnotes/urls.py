"""
URL configuration for sportnotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from swingtime import event_view
from training.views import competitions, add_competitions, add_discipline, showTrainings, sport_events, add_training, delete_training, add_approach, setCompleted, show_training_plan, main, all_events, add_event
from authorization.views import auth, out, reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('main/', main),

    path('training/', showTrainings),
    path('auth/', auth),
    path('reg/', reg),
    path('out/', out),
    
    path('competitions_list/', competitions),
    path('add_competitions/', add_competitions),
    path('add_discipline/', add_discipline),

    path('add_training/', add_training),
    path('training/delete_training/', delete_training),
    path('training/add_approach/', add_approach),
    path('training/setCompleted/', setCompleted),

    path('training_plans/', show_training_plan),


    path('events/', sport_events),
    path('', include('swingtime.urls')),
    # path(' path("calender/", views.CalendarViewNew.as_view(), name="calendar"),', include('swingtime.urls'))
    
    
    path('all_events/', all_events, name="all_events"),
    path('add_event/', add_event, name="add_event"),
]
