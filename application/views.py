from django.shortcuts import redirect, render
from admin_app.models import edu, intern, home, skill, query
from datetime import datetime



def home_page(request):
    home_page = home.objects.all()
    return render(request, "home.html", {'form':home_page})


def resume(request):
    return render(request, "resume.html")


def education(request):
    form = edu.objects.all()
    return render(request, "education.html", {'form':form})


def internship(request):
    interns = intern.objects.all()
    return render(request, "intern.html", {'form':interns})


def work(request):
    return render(request, "work_exp.html")


def skil(request):
    wet = skill.objects.all()
    return render(request, "skill.html", {'form': wet})


def contact(request):
    return render(request, "contact.html")

def customer_qa(request):
    x = datetime.now
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['mail']
        qu = request.POST['qu']
        time = request.POST['time']
        form = query(name = name, email = email, qu = qu, time = time).save()
        return redirect('/query')
    return render(request, "query.html", {'x':x})