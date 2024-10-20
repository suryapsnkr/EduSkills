from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def register(request):
    return render(request, 'register.html')

def rsubmit(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        mname = request.POST["mname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        adhar = request.POST["adhar"]
        pan = request.POST["pan"]
        password = request.POST["pass1"]
        heq = request.POST["heq"]
        experience= request.POST["experience"]

        user = User.objects.create_user(username = email, password = password)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()

        student = Student.objects.create(fname = fname, mname = mname, lname = lname, email = email, phone = mobile, adhar = adhar, pan = pan, password = password, heq = heq, experience = experience)

    return redirect("/")       


def handelLogout(request):
    logout(request)
    return redirect("/")

def handelLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/")

    return HttpResponse("404- Not found")


