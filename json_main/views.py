from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,redirect

from json_main.models import UserModel

def json_main(request):

    try:
        username = request.session['user_name']
        
    except:
        username = "user"

    log = ""

    if logedin(request):
        log = "Logout"
        print("lol logout")

    return render(request,'index.html',{"user_name":username,"logedin":log})


def profile(request):

    if logedin(request):
        template = loader.get_template('profile.html')
        return HttpResponse(template.render())
    else:
        return redirect("../login")

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def login(request):
    template = loader.get_template('login.html')
    return render(request,'login.html',{"error":""})

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


def signup(request):

    template = loader.get_template('sign_up.html')
    return HttpResponse(template.render())

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


def login_val(request):

    if(request.method == 'GET'):

        email = request.GET['email']
        password = request.GET['password']

        l = UserModel.objects.raw("SELECT * FROM json_main_usermodel WHERE user_email = '{}' AND user_password = '{}'".format(email,password))
        # print(l[0].user_name)

        try:
            request.session['user_name'] = l[0].user_name
            request.session['user_email'] = l[0].user_email
        except:
            print("lol login")
            # return redirect("../login",{"error":"USER DOESN'T EXIST"})
            return render(request,'login.html',{"error":"USER DOESN'T EXIST"})
        
        return redirect("../")
        
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


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
    
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def logout(request) :

    try:
        request.session['user_name'] = None
        request.session['user_email'] = None
        del request.session['your key']
    except:
        print("ERROR")

    return redirect("../login")


# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def logedin(request):
    
    t = True

    try:
        if request.session['user_name'] != None :
            t = True
        else:
            t = False
    except:
        t = False

    return t

