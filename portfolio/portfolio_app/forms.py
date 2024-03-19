from django import forms 
from django.forms import ModelForm 
from .models import Project, Portfolio, Student

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'portfolio']