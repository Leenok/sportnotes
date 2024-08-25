from django.contrib import admin
from training.models import Discipline, Competition, Training, Exercise, Program, Approach, TrainingPlan, TrainingLine, BasicApproach, NewTraining, NewTrainingLine, NewApproach

# Register your models here.
class my_discipline(admin.ModelAdmin):
    list_display = ["name"]

class my_competition(admin.ModelAdmin):
    list_display = ["sportsmen", "name", "date_start", "city", "discipline", "plan_result", "plan_place", "result"]

admin.site.register(Competition, my_competition)
admin.site.register(Discipline, my_discipline)
admin.site.register(Training)
admin.site.register(Exercise)
admin.site.register(Program)
admin.site.register(Approach)

admin.site.register(TrainingPlan)
admin.site.register(TrainingLine)
admin.site.register(BasicApproach)

admin.site.register(NewTraining)
admin.site.register(NewTrainingLine)
admin.site.register(NewApproach)