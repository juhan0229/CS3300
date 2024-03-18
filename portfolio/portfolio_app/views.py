from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
# Render the HTML template index.html with the data in the context variable.
    return render(request, 'portfolio_app/index.html')

def login():
    return HttpResponse('login page')

def logout():
    return HttpResponse('logout page')

# New view for creating a project
def create_project(request):
    if request.method == 'POST':
        # Process form data and save the new project
        pass  # Replace this with your actual code if you have a form
    else:
        # Render the form to create a new project
        form = ProjectForm()  # Use your project form here if you have one
        return render(request, 'portfolio_app/create_project.html', {'form': form})

def view_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio_app/view_project.html', {'project': project})

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        # Process form data and update the project
        pass  # Replace this with your actual code
    else:
        # Render the form to update the project
        return render(request, 'portfolio_app/update_project.html', {'project': project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    # Delete the project
    pass  # Replace this with your actual code