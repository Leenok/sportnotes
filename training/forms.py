
from selectors import SelectSelector
from .models import Competition, Discipline, Approach
from django.forms import ChoiceField, HiddenInput, DateInput, ModelForm, TextInput, DateTimeInput, NumberInput


class ApproachForm(ModelForm):
    class Meta:
        model = Approach
        fields = ['training_id', 'programm_id', 'number', 'quantity', 'weight', 'time', 'time_rest', 'isCompleted']

        widgets = {
            'training_id': HiddenInput(),
            'programm_id': HiddenInput(),
            # 'training_id': NumberInput(attrs={
            #     'class': 'form-control', 
            #     'placeholder': 'training_id'
            # }),
            # 'programm_id': NumberInput(attrs={
            #     'class': 'form-control', 
            #     'placeholder': 'номер'
            # }),
            'number': NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'номер'
            }),
            'quantity': NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'раз'
            }),
            'weight': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'кг'
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
