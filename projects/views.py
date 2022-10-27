from django.shortcuts import render , redirect
from django.db.models import Q


from .models import Project,Tag
from.forms import ProjectForm
# Create your views here.





def projects(request):
    
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags=Tag.objects.filter(name__icontains = search_query)

    projects=Project.objects.distinct().filter(
        Q(title__icontains = search_query)|
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tags)
     )
    # projects=Project.objects.all()
    # tags=Tag.objects.all()[0:4]
    context={'projects':projects ,'tags':tags}

  

    return render(request, 'projects/projects.html', context)



def project(request ,pk):
    projectObj = Project.objects.get(id=pk)
    context ={'project':projectObj,}
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form=ProjectForm()
    tags=Tag.objects.all()
    if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('projects')
   
    context ={'form':form  , 'tags':tags}
    return render(request, "projects/project_form.html", context)


def updateProject(request ,pk):
    project =Project.objects.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST ,request.FILES, instance=project)
        if form.is_valid():
                form.save()
                return redirect('projects')

    context ={'form':form}
    return render(request,  "projects/project_form.html", context)            


def deleteProject(request ,pk):
    project = Project.objects.get(id=pk)
    
    if request.method == 'POST':
           project.delete()
           return redirect('projects')
    context ={'object':project} 
    return render(request, 'delete.html', context)   