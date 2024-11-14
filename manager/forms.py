from django import forms
from date.models import Addition

class additionFormClass(forms.Form):
    ID = forms.StudentID()  
    name = forms.name()
    Class = forms.Class()
    address =forms.address()
