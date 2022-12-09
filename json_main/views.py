from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,redirect

from json_main.models import UserModel, saved_jsons

def json_main(request):

    try:
        username = request.session['user_name']
        user_id = request.session['user_id']
    except:
        username = "user"
        user_id = None
        
    log = ""

    if logedin(request):
        log = "Logout"

    return render(request,'index.html',{"user_id":user_id,"user_name":username,"logedin":log})

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def profile(request):

    if logedin(request):
        template = loader.get_template('profile.html')
        # data = saved_jsons.objects.filter(id = request.session['user_id']).get()
        data = saved_jsons.objects.raw(" SELECT * FROM json_main_saved_jsons WHERE user_id = {}".format(request.session['user_id']))
        print(len(data))
        return render(request,'profile.html',{"data":data})
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
    return render(request,'sign_up.html')
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


def login_val(request):

    if(request.method == 'POST'):

        email = request.POST['email']
        password = request.POST['password']

        # l = UserModel.objects.raw("SELECT * FROM json_main_usermodel WHERE user_email = '{}' AND user_password = '{}'".format(email,password))
        # print(l[0].user_name)

        obj = UserModel.objects.filter(user_email = email , user_password = password).get()

        try:
            request.session['user_name'] = obj.user_name
            request.session['user_email'] = obj.user_email
            request.session['user_id'] = obj.pk
        except :
            print("lol login")
            # return redirect("../login",{"error":"USER DOESN'T EXIST"})
            return render(request,'login.html',{"error":"USER DOESN'T EXIST"})
        
        return json_main(request)
        # return redirect("../")
        
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


def sign_up_val(request):

    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        # obj = UserModel(user_name = name , user_email = email , user_password = password)
        # obj = UserModel(name,email,password)
        obj = UserModel()
        obj.user_name = name
        obj.user_email = email
        obj.user_password = password 

        obj.save()

        # l = UserModel.objects.raw("SELECT id FROM json_main_usermodel WHERE user_email = '{}'".format(email))
        obj = UserModel.objects.filter(user_email = email).get()


        request.session['user_id'] = obj.pk
        request.session['user_name'] = name
        request.session['user_email'] = email

        return redirect("../")
    
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def logout(request) :

    try:
        request.session['user_name'] = None
        request.session['user_email'] = None
        request.session['user_id'] = None
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

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def save_fun(user_id,json_str):

    # print("INSERT INTO json_main_saved_jsons (user_id,saved_json) VALUES ({},'{}')".format(user_id,json_str))
    # l = saved_jsons.objects.raw("INSERT INTO json_main_saved_jsons(user_id,saved_json) VALUES ({},'{}')".format(user_id,json_str))
    # print(user_id)

    obj_user = UserModel.objects.filter(id = user_id).get()
    obj_user.saved_jsons_set.create(saved_json = json_str)

    # obj = saved_jsons()
    # obj.user_id = obj_user.user_id
    # obj.saved_json = json_str

    # obj.save()


# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def save(request):

    if logedin(request):
        json_str = request.POST['formatted']
        user_id = request.session['user_id']
        save_fun(user_id,json_str)
        return redirect("../")
    else :
        return redirect("../login")

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def delete_fun(id):

    obj_user = saved_jsons.objects.filter(id = id).get()
    obj_user.delete()

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def delete(request,id):

    if logedin(request):
        delete_fun(id)
        return redirect("../profile")
    else :
        return redirect("../login")
