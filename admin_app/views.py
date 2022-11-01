from symbol import return_stmt
from turtle import heading
from django.shortcuts import redirect, render
from admin_app.models import edu, intern, home, skill, query
from django.contrib import messages 
username = "surya"
passwor = "1234"


def authn(request):
    if request.method == "POST":
        name = request.POST['name']
        passw = request.POST['password']
        if (username==name) and (passwor == passw):
            return redirect('/guardian/home/')
        else:
            messages.error(request, "invalid, user....!!!!!!!!!!!")
    return render(request, "auth.html")        


def ad_home(request):
    form = home.objects.all()
    if request.method == "POST":
        name = request.POST['heading']
        board = request.POST['content']
        home(heading=name, content=board).save()
        return redirect('/guardian/home')
    return render(request, "admin_home.html", {'form': form})


def ad_home_update(request, id):
    hom = home.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['heading']
        board = request.POST['content']
        form = home.objects.filter(id=id).update(
            heading=name, content=board,)
        return redirect('/guardian/home')
    return render(request, "admin_home_update.html", {'form': hom})


def ad_home_delete(request, id):
    form = home.objects.get(id=id)
    form.delete()
    return redirect('/guardian/home')


def ad_resume(request):
    return render(request, "admin_resume.html")


def ad_education(request):
    form = edu.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        board = request.POST['board']
        yop = request.POST['yop']
        mark = request.POST['mark']
        degree = request.POST['degree']
        edu(name=name, board=board, yop=yop, mark=mark, degree=degree).save()
        return redirect('/guardian/education/')
    return render(request, "admin_education.html", {'form': form})


def ad_education_update(request, id):
    educat = edu.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        board = request.POST['board']
        yop = request.POST['yop']
        mark = request.POST['mark']
        degree = request.POST['degree']
        form = edu.objects.filter(id=id).update(
            name=name, board=board, yop=yop, mark=mark, degree=degree)
        return redirect('/guardian/education')
    return render(request, "admin_education_update.html", {'form': educat})


def ad_education_delete(request, id):
    form = edu.objects.get(id=id)
    form.delete()
    return redirect('/guardian/education/')


def ad_intern(request):
    form = intern.objects.all()
    if request.method == "POST":
        name = request.POST['com']
        board = request.POST['period']
        yop = request.POST['inn']
        intern(com=name, period=board, inn=yop).save()
        return redirect('/guardian/intern/')
    return render(request, "admin_intern.html", {'form': form})


def ad_intern_update(request, id):
    inter = intern.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['com']
        board = request.POST['period']
        yop = request.POST['inn']
        form = intern.objects.filter(id=id).update(
            com=name, period=board, inn=yop)
        return redirect('/guardian/intern')
    return render(request, "admin_intern_update.html", {'form': inter})


def ad_intern_delete(request, id):
    form = intern.objects.get(id=id)
    form.delete()
    return redirect('/guardian/intern/')


def ad_skill(request):
    sk = skill.objects.all()
    if request.method == "POST":
        skil = request.POST['skill']
        form = skill(ski=skil).save()
        return redirect('/guardian/skill')
    return render(request, "admin_skill.html", {'form': sk})


def ad_skill_update(request, id):
    sk = skill.objects.get(id=id)
    if request.method == "POST":
        skil = request.POST['skill']
        form = skill.objects.filter(id=id).update(ski=skil)
        return redirect('/guardian/skill')
    return render(request, "admin_skill_update.html", {'form': sk})


def ad_skill_delete(request, id):
    form = skill.objects.get(id=id)
    form.delete()
    return redirect('/guardian/skill')


def ad_query(request):
    qua = query.objects.all()
    return render(request, "admin_query.html", {"form": qua})

def ad_query_delete(request, id):
    form = query.objects.get(id = id)
    form.delete()
    return redirect('/guardian/query')

def ad_work(request):
    return render(request, "admin_work_exe.html")
