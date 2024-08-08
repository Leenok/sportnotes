from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    count_approach = models.IntegerField(null=True, blank=True)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Training(models.Model):
    sportsmen = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    type = models.CharField(max_length=100)
    programm_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Approach(models.Model):
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE, default=None)
    programm_id = models.ForeignKey(Program, on_delete=models.CASCADE, default=None)
    number = models.IntegerField(default=None, blank=True, null=True) #номер
    quantity = models.IntegerField(default=None, blank=True, null=True) #кол-во
    weight = models.FloatField(default=None, blank=True, null=True) #вес
    distance = models.FloatField(default=None, blank=True, null=True) #дистанция
    time = models.FloatField(default=None, blank=True, null=True) #время
    time_rest = models.FloatField(default=None, blank=True, null=True) #время отдыха
    isCompleted = models.BooleanField(default=False) #выполнен ли подход
    

class Discipline(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Competition(models.Model):
    sportsmen = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    name = models.CharField(max_length=100)
    date_start = models.DateField(default=None)
    date_end = models.DateField(default=None)
    city =  models.CharField(max_length=100)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    plan_result = models.CharField(max_length=100)
    plan_place = models.CharField(max_length=100)
    place = models.CharField(max_length=100, blank=True)
    result = models.CharField(max_length=100, blank=True)
    result_first_place = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    imgage = models.ImageField(upload_to="app1/static/img/competition", blank=True)

    def __str__(self):
        return self.name
    
    # def getUserId(self):
    #     userId = self.request.user
    #     return userId

