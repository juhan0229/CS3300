from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio, Project, Student
from .forms import PortfolioForm, ProjectForm


# Create your views here.
def index(request):
    active_portfolios = Portfolio.objects.filter(active=True)
    return render(request, 'portfolio_app/index.html', {'active_portfolios': active_portfolios})

def login():
    return HttpResponse('login page')

def logout():
    return HttpResponse('logout page')

class StudentDetailView(generic.DetailView): 
    model = Student 

def portfolio_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    return render(request, 'portfolio_app/portfolio_detail.html', {'portfolio': portfolio})

def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save()
            return redirect('portfolio_detail', portfolio_id=portfolio.id)
    else:
        form = PortfolioForm()
    return render(request, 'portfolio_app/create_portfolio.html', {'form': form})

def create_project(request, portfolio_id):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = Portfolio.objects.get(pk=portfolio_id)
            project.save()
            return redirect('portfolio_detail', portfolio_id=portfolio_id)
    else:
        form = ProjectForm()
    return render(request, 'portfolio_app/create_project.html', {'form': form})

def view_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio_app/view_project.html', {'project': project})

def update_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('view_project', project_id=project_id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio_app/update_project.html', {'form': form})

def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_detail', portfolio_id=project.portfolio.id)
    return render(request, 'portfolio_app/delete_project.html', {'project': project})

def delete_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('index')
    return render(request, 'portfolio_app/delete_portfolio.html', {'portfolio': portfolio})

def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'portfolio_app/student_detail.html', {'student': student})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'portfolio_app/create_student.html', {'form': form})

def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student_id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'portfolio_app/update_student.html', {'form': form})

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'portfolio_app/delete_student.html', {'student': student})
