
from random import choice
import select
from django import forms
from selectors import SelectSelector
from .models import Competition, Discipline, Approach, Training, Program, TrainingLine, BasicApproach, TrainingPlan, NewTraining, NewTrainingLine, NewApproach
from django.forms import ChoiceField, HiddenInput, DateInput, ModelForm, TextInput, DateTimeInput, NumberInput

class NewApproachForm(ModelForm):
    class Meta:
        model = NewApproach
        fields = ['line_id', 'number', 'quantity', 'weight', 'distance', 'type_temp', 'time', 'time_rest']

        widgets = {
            'line_id': HiddenInput(),
            'number': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Номер подхода'
            }),
            'quantity': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Раз'
            }),
            'weight': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Вес'
            }),
            'distance': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'км'
            }),
            'type_temp': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'темп'
            }),
            'time': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'мин'
            }),
            'time_rest': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Отдых мин'
            }),
        }


class NewTrainingLineForm(ModelForm):
    class Meta:
        model = NewTrainingLine
        fields = ['training_id', 'exercise_id', 'type_of_approaches']

        widgets = {
            'training_id': HiddenInput(),
            'exercise_id': HiddenInput(),
        }

class NewTrainingForm(ModelForm):
    class Meta:
        model = NewTraining
        fields = ['sportsmen_id', 'training_date', 'training_plan_id', 'training_description']

        widgets = {
            'sportsmen_id': HiddenInput(),
            # 'training_plan_id': HiddenInput(),
            'name': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Название'
            }),
            'training_date': DateInput(
                format=['%d-%m-%Y'],
                attrs={'type':'date',
                        'class': 'form-control', 
                        'placeholder': 'Дата тренировки',
            }),
            'training_description': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Описание'
            }),
        }

class TrainingPlanForm(ModelForm):
    class Meta:
        model = TrainingPlan
        fields = ['sportsmen_id', 'name', 'isPublic']

        widgets = {
            'sportsmen_id': HiddenInput(),
            'name': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Название'
            }),
            'isPublic': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Публичный'
            }),
        }

class BasicApproachForm(ModelForm):
    class Meta:
        model = BasicApproach
        fields = ['training_line_id', 'number', 'quantity', 'weight', 'distance', 'type_temp', 'time', 'time_rest']

        widgets = {
            'training_line_id': HiddenInput(),
            'number': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Номер подхода'
            }),
            'quantity': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Раз'
            }),
            'weight': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Вес'
            }),
            'distance': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'км'
            }),
            'type_temp': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'темп'
            }),
            'time': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'мин'
            }),
            'time_rest': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Отдых мин'
            }),
        }

class TrainingLineForm(ModelForm):
    class Meta:
        model = TrainingLine
        fields = ['training_plan_id', 'exercise_id', 'type_of_approaches']

        widgets = {
            'training_plan_id': HiddenInput(),
            'type_of_approaches': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Тип подхода'
            }),
        }

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'count_approach', 'repeat', 'exercise_id']

        widgets = {
            'name': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Название программы'
            }),
            'count_approach': NumberInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Колличество подходов'
            }),
            'repeat': NumberInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Колличество повторений'
            }),

        }

class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ['sportsmen', 'name', 'date', 'type', 'programm_name']

        widgets = {
            'sportsmen': HiddenInput(),
            'name': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Название тренировки'
            }),
            'date': DateInput(
                format=['%d-%m-%Y'],
                attrs={'type':'date',
                        'class': 'form-control', 
                        'placeholder': 'Дата  тренировки',
                #    'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
            }),
            'type': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Тип тренировки'
            }),
            # 'programm_name': TextInput(attrs={
            #     'class': 'intput_competition',
            #     'placeholder': 'Программа тренировки'
            # }),

        }

class ApproachForm(ModelForm):
    class Meta:
        model = Approach
        fields = ['training_id', 'programm_id', 'number', 'weight', 'quantity', 'distance', 'time', 'time_rest', 'isCompleted']

        widgets = {
            'training_id': HiddenInput(),
            'programm_id': HiddenInput(),
            'number': NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'номер'
            }),
            'weight': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'кг'
            }),
            'quantity': NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'раз'
            }),
            'distance': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'дистанция'
            }),
            'time': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'время'
            }),
            'time_rest': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'время отдыха'
            }),
        }

class DisciplineForm(ModelForm):
    class Meta:
        model = Discipline
        fields = ['name', 'description']

class CompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'date_start', 'date_end', 'city', 'discipline', 'plan_result', 'plan_place', 'place', 'result', 'result_first_place', 'description']
        
        widgets = {
            'name': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Название соревнований'
            }),
            'date_start': DateInput(
                format=['%d-%m-%Y'],
                attrs={'type':'date',
                        'class': 'form-control', 
                       'placeholder': 'Дата  начала соревнований',
                    #    'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
            'date_end': DateInput(
                format=['%d-%m-%Y'],
                attrs={'type':'date',
                        'class': 'form-control', 
                       'placeholder': 'Дата окончаний соревнований',
                    #    'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
            'city': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Город соревнований'
            }),
            # 'discipline': SelectSelector(
            #     attrs={
            #         'choices': 'TITLE_CHOICES'
            #     # choices=TITLE_CHOICES
            #     # 'class': 'intput_competition',
            #     # 'placeholder': 'Дисциплина'
            # }
            # ),
            'plan_result': NumberInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Планируемый результат'
            }),
            'plan_place': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Планируемое место'
            }),
            'place': NumberInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Занято место'
            }),
            'result': NumberInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Результат'
            }),
            'result_first_place': NumberInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Результат первого места'
            }),
            'description': TextInput(attrs={
                'class': 'intput_competition',
                'placeholder': 'Итоги выступления'
            })
        }
