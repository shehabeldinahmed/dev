from django.shortcuts import render
from django.db.models import Q
from .models import Profile, Message ,Skill

# Create your views here.
def profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )


    context = {'profiles': profiles, 'search_query': search_query,}
    
    return render(request, 'users/profiles.html', context)




def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request, 'users/user-profile.html', context)


def userAccount(request):
    
    context={} 
    return render(request, 'users/account.html', context)


def editAccount(request):
    context={} 
    return render(request, 'users/profile_form.html', context)


def createSkill(request):
    context={} 
    return render(request, 'users/skill_form.html', context)


def updateSkill(request, pk):
    context={} 
    return render(request, 'users/skill_form.html', context)


def deleteSkill(request, pk):
    context={} 
    return render(request, 'delete_template.html', context)


def inbox(request):
    context={} 
    return render(request, 'users/inbox.html', context)


def viewMessage(request, pk):
    context={} 
    return render(request, 'users/message.html', context)



def createMessage(request, pk):
    context={} 
    return render(request, 'users/message_form.html', context)