from django import forms 
from django.forms import ModelForm 
from .models import Project, Portfolio

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'screenshot', 'technologies']

        
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'url']
