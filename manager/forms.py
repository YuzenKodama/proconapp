from django import forms
from login.models import CustomUser
class additionFormClass(forms.Form):
    ID = forms.StudentID()  
    name = forms.name()
    Class = forms.Class()
    address =forms.address()
