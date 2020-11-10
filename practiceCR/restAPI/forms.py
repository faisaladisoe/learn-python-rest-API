from django import forms
from django.forms import ModelForm
from .models import Biodata, Layouting

class BiodataForm(ModelForm):
    class Meta:
        model = Biodata
        fields = '__all__'
    
class LayoutForm(ModelForm):
    class Meta:
        model = Layouting
        fields = '__all__'
    
    search = forms.CharField(
        required = False,
        max_length = 50,
        widget = forms.TextInput(
            attrs = {
                'id' : 'search',
                'placeholder' : 'find your friends',
                'autocomplete' : 'off',
            }
        )
    )
    
    GROUP_CHOICES = (
        ('All', 'All'),
        ('12 IPA 1', '12 IPA 1'),
        ('12 IPA 2', '12 IPA 2'),
        ('12 IPA 3', '12 IPA 3'),
        ('12 IPA 4', '12 IPA 4'),
        ('12 IPA 5', '12 IPA 5'),
        ('12 IPA 6', '12 IPA 6'),
        ('12 IPA 7', '12 IPA 7'),
        ('12 IPA 8', '12 IPA 8'),
        ('12 IPS', '12 IPS'),
    )
    groupby = forms.ChoiceField(
        required = False,
        choices = GROUP_CHOICES,
        widget = forms.Select(
            attrs = {
                'id' : 'groupby'
            }
        )
    )

    SORTING_CHOICES = (
        ('Ascending', 'Ascending'),
        ('Descending', 'Descending'),
    )
    sorting = forms.ChoiceField(
        required = False,
        choices = SORTING_CHOICES,
        widget = forms.Select(
            attrs = {
                'id' : 'sorting'
            }
        )
    )
        