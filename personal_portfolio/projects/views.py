# projects/views.py

from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all() # this a querry that selects all the objects in the projects table
    context = {
        "projects": projects
    } #define a dictionary named context. The dictionary only has one entry, projects, to which you assign your Queryset containing all the projects. Django uses the context dictionary to send information to your template.
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)