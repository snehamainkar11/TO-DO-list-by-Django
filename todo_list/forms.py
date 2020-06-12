
from django import forms
from .models import List ,Feedback

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
 
class FeedbackForm(forms.ModelForm):
 
    class Meta:
        model = Feedback
        fields = '__all__'