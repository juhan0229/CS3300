from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Portfolio, Project, Student
from .forms import PortfolioForm, ProjectForm, StudentForm
from django.views import generic


# Create your views here.
def index(request):
    active_portfolios = Portfolio.objects.filter(is_active=True)
    return render(request, 'portfolio_app/index.html', {'active_portfolios': active_portfolios})

def login(): 
    return render("Login") 

def logout(): 
    return render("Logout") 

class StudentDetailView(generic.DetailView): 
    model = Student 
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'


def student_list(request):
    students = Student.objects.all()
    return render(request, 'portfolio_app/student_list.html', {'students': students})


def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    # Fetch related projects
    projects = portfolio.project_set.all()  
    return render(request, 'portfolio_app/portfolio_detail.html', {'portfolio': portfolio, 'projects': projects})

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
            return redirect('portfolio_detail', pk=portfolio_id)  
    else:
        form = ProjectForm()
    return render(request, 'portfolio_app/create_project.html', {'form': form})

def view_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio_app/view_project.html', {'project': project})

def update_project(request, pk):  
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('view_project', project_id=pk)  
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio_app/update_project.html', {'form': form})



def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_detail', pk=project.portfolio.pk)
    return render(request, 'portfolio_app/delete_project.html', {'project': project})

def delete_project_confirmation(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio_app/delete_project.html', {'project': project})



def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'portfolio_app/student_detail.html', {'student': student})

def update_portfolio(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_detail', pk=pk) 
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio_app/update_portfolio.html', {'form': form})