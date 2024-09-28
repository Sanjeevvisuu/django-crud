from django import forms
from rest_app.models import *

class create_student(forms.ModelForm):
    class Meta:
        model=students
        fields="__all__"