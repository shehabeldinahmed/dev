from django.shortcuts import render

# Create your views here.
def projects(request):
    context ={}
    return render (request ,'projects.html',context)


# Create your views here.
def project(request , pk):
    context ={}
    return render (request ,'project.html',context)
