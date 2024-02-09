from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login as auth_login,logout
from .models import Register_User, Fill_Form
from .forms import Fill_FormForm
from django.views import View

class Form(View):
    def get(self,request):
        form = Fill_FormForm()
        return render(request,'form.html',{'form':form})
    def post(self,request):
        form = Fill_FormForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('form')
        else:
            return render(request,'form.html',{'form':form})


# Create your views here.
# for index page
def index(request):
    return render(request,'index.html')

#  for about page
def about(request):
    return render(request,'about.html')

# for registration page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Taken ')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            return render(request,'login.html')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

# for login page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')



#
def newpage(request):
    if request.method == 'POST':
        form=userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'newpage.html')
            print("form submitted")
        else:
            print("form not submitted")
            return render(request,'newpage.html')
    else:
        form=UserCreationForm()
        return render(request,'newpage.html',{'form':form})

    return render(request,'newpage.html')



# for form filling
def form(request):
    if request.method == 'POST':
        user_name=request.POST['user_name']
        date_of_birth=request.POST['date_of_birth']
        age=request.POST['age']
        gender=request.POST['gender']
        phone_number=request.POST['phone_number']
        mail_id=request.POST['mail_id']
        address=request.POST['address']
        district=request.POST['district']
        branch=request.POST['branch']
        type_of_account=request.POST['type_of_account']
        materials_provided=request.POST['materials_provided']
        form=Fill_Form(user_name=user_name,date_of_birth=date_of_birth,age=age,gender=gender,phone_number=phone_number,mail_id=mail_id,address=address,district=district,branch=branch,type_of_account=type_of_account,materials_provided=materials_provided)
        form.save()
        messages.info(request,'form submitted')
        return render(request,'submit.html')
    else:
        return render(request,'form.html')

#
#   # Replace with the actual name of your form
# def form(request):
#     if request.method == 'POST':
#         form = Fill_FormForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Form submitted successfully')
#             return redirect('form')
#         else:
#             return render(request, 'form.html', {'form': form})
#     else:
#         form = Fill_FormForm()
#         return render(request, 'form.html', {'form': form})
#
# def form(request):
#     return redirect('form')

def submit(request):
    return render(request,'submit.html')


