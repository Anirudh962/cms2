from django.shortcuts import redirect, render
from .models import course_outcomes
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def home(request):
    return render(request,"home.html",{'request': request})

def insertco(request):
    vtucname= request.POST['tucname']; 
    vtudes = request.POST['tudes'];
    vtuchours = request.POST['tuchours'];
    vtumarks = request.POST['tumarks'];
    co = course_outcomes(course_name=vtucname,description=vtudes,contact_hours=vtuchours,marks=vtumarks);
    co.save();
    return redirect('view_co')

def view_co(request):
    # Fetch all courses from the database
    courses = course_outcomes.objects.all()
    return render(request, 'home.html', {'courses_outcomes': courses})

def deleteprofile(request,course_name):
    courses_name=course_outcomes.objects.get(course_name=course_name)
    courses_name.delete()
    return redirect("view_co")

def editprofile(request, course_name):
  course = course_outcomes.objects.get(course_name=course_name)
  return render(request,"editprofile.html",{'course':course})

def updateco(request, course_name):
    ntucname= request.POST['tucname']; 
    ntudes = request.POST['tudes'];
    ntuchours = request.POST['tuchours'];
    ntumarks = request.POST['tumarks'];
    co = course_outcomes.objects.get(course_name=course_name)
    co.course_name=ntucname
    co.description=ntudes
    co.contact_hours=ntuchours
    co.marks=ntumarks
    co.save();
    return redirect('view_co')



    

