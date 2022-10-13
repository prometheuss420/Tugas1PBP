from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import random;
import datetime
from todolist.models import Task
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    img_title = ""
    a = random.randrange(2)
    if a == 1:
        img_title = "https://cdn.discordapp.com/attachments/1027273502060982372/1027415564823576638/undraw_Push_notifications_re_t84m.png"
    elif a == 2:
        img_title = "https://cdn.discordapp.com/attachments/1027273502060982372/1027415565188485151/undraw_Problem_solving_re_4gq3.png"
    else:
        img_title = "https://cdn.discordapp.com/attachments/1027273502060982372/1027415565511430154/undraw_Feedback_re_urmj.png"

    context = {
    'username' : request.user,
    'last_login': request.COOKIES['last_login'],
    'img_title' : img_title,
    }
    return render(request, "todolist.html",context)


@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_task(request,id):
    if request.method == 'DELETE':
        Task.objects.filter(pk=id).delete()
        return HttpResponse(status=202)


@login_required(login_url='/todolist/login/')
def change_status(request,id):
    status_change = Task.objects.filter(pk=id).get()
    if status_change.is_finished == "Belum Selesai":
        Task.objects.filter(pk=id).update(is_finished = "Selesai")
    else:
        Task.objects.filter(pk=id).update(is_finished = "Belum Selesai")
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title != "" and description != "":
            Task.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user, is_finished="Belum Selesai")
            return HttpResponseRedirect(reverse("todolist:show_todolist")) 
        
        if title == "" and description == "":
            messages.info(request, 'Judul dan Deskripsi tidak boleh kosong!')
        elif title == "":
            messages.info(request, 'Judul tidak boleh kosong!')
        else:
            messages.info(request, 'Deskripsi tidak boleh kosong!')

            
    return render(request, "add_task.html")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = Task.objects.create(title = title, description = description, date = datetime.date.today(), user=request.user, is_finished="Belum Selesai")
        new_task = {
            'pk' : new_task.pk,
            'fields':{
                'title':new_task.title,
                'description':new_task.description,
                'date':new_task.date,
                'is_finished':new_task.is_finished

            }
        }
        return JsonResponse(new_task);

