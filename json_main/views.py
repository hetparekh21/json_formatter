from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,redirect

from json_main.models import UserModel

def json_main(request):

    try:
        username = request.session['user_name']
        
    except:
        username = "user"

    return render(request,'index.html',{"user_name":username})



def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())



def signup(request):

    template = loader.get_template('sign_up.html')
    return HttpResponse(template.render())


def login_val(request):

    if(request.method == 'GET'):

        email = request.GET['email']
        password = request.GET['password']

        l = UserModel.objects.raw("SELECT * FROM json_main_usermodel WHERE user_email = '{}' AND user_password = '{}'".format(email,password))

        # print(l[0].user_name)
        request.session['user_name'] = l[0].user_name
        request.session['user_email'] = l[0].user_email
        
        return redirect("../")
        


def sign_up_val(request):

    if(request.method == 'GET'):
        name = request.GET['name']
        email = request.GET['email']
        password = request.GET['password']

        # obj = UserModel(user_name = name , user_email = email , user_password = password)
        # obj = UserModel(name,email,password)
        obj = UserModel()
        obj.user_name = name
        obj.user_email = email
        obj.user_password = password 

        obj.save()
        request.session['user_name'] = name
        request.session['user_email'] = email

        return redirect("../")
    

# def bool logedin():


