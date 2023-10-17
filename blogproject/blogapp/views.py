from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .forms import Registationform
from .models import User,Blog
from django.http import HttpResponseRedirect

class UserList(ListView):
    template_name = "User_list.html"
    model=User
    context_object_name = "a"

def home(request):
    return render(request,"login.html")

def loginpage(request):
    return render(request,"register.html")


def updateuser(request,id):
    request.session['uid'] = id
    rec=User.objects.get(id=id)
    form = Registationform(instance=rec)
    return render(request, 'admin_update_user.html', {"form": form, "id": id})


def updateuserform(request):
    rtos = User.objects.get(pk=request.session['uid'])
    form = Registationform(request.POST, instance=rtos)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/display')
    return render(request,'rejected.html',{"id":id})


def edituserform(request):
    rtos = User.objects.get(pk=request.session['uid'])
    form = Registationform(request.POST, instance=rtos)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/homepage')
    return render(request,'rejected.html',{"id":id})



def deleteuser(request,id):
    a = User.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect('/display')


def homepage(request):
    return render(request,"home.html")


def adminhome(request):
    return render(request,"adminhome.html")

def postblog(request):
    return render(request, "user_post_blog.html")




def Registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number = request.POST.get('number')
        passwords=request.POST.get('password')
        val = User(name=name,email=email,phone=number,pswd=passwords)
        val.save()
        obj = User.objects.filter(email=email, pswd=passwords)
        if obj.filter(email=email, pswd=passwords).exists():
            for i in obj:
                id = i.id
                name = i.name
                email = i.email
                request.session['uid'] = id
                request.session['email'] = email
                request.session['name'] = name
                return render(request, 'home.html')
    else:

        return render(request, 'login.html')

def postnewblog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        userid = request.session['id']
        useremail = request.session['email']
        username =request.session['name']
        val = Blog(userid=userid , username = username,useremail = useremail,blogtitle= title,blogcontent=content)
        val.save()
        return render(request, 'home.html')

class BlogList(ListView):
    template_name = "user_view_blog.html"
    model=Blog
    context_object_name = "b"


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = User.objects.filter(email=email, pswd=password)
        if obj.filter(email=email, pswd=password).exists():
            for i in obj:
                id = i.id
                name= i.name
                emaill = i.email
                password = i.pswd
                request.session['email'] = emaill
                request.session['id'] = id
                request.session['name'] = name
                if email == 'admin@gmail.com' and password == 'admin':
                    uname = {'uname': 'Admin', 'uemail': 'admin@gmail.com'}
                    return render(request, "adminhome.html",uname)
                else:
                    uname = {'uname' : request.session['name'],'uemail': request.session['email']}
                    return render(request, "home.html",uname,)
        else:
            return render(request, "usernotfound.html")



def userpostedblogs(request):
    myblogs = Blog.objects.filter(userid=request.session['id'])
    return render(request, "user_posted_blogs_list.html", {"a": myblogs})


def editblog(request,id):
    rec = Blog.objects.filter(id=id)
    for i in rec:
        request.session['blogid'] = i.id
    return render(request, "user_update_blog.html", {"a": rec})

def postupdateblog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        blogid = request.session['blogid']
        Blog.objects.filter(id=blogid).update(blogtitle=title,blogcontent=content)
        return HttpResponseRedirect('/userpostedblogs')




def deleteBlog(request,id):
    a = Blog.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect('/userpostedblogs')

def edituserprofile(request,id):
    obj = User.objects.get(id=id)
    form = Registationform(instance=obj)
    return render(request, 'user_edit_profile.html', {"form": form})




