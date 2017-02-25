from django import forms
from models import *

class Complaintform(forms.ModelForm):
    class Meta:
        model=Complaint
