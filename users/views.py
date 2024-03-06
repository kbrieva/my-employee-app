from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.core.exceptions import  ObjectDoesNotExist

def index(request):
    user_list   = User.objects.order_by('-pub_date')[:5]
    context = {'user_list': user_list}
    return render(request, 'users/index.html', context)

def add(request):
    return render(request, 'users/add.html')

def processAdd(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    position = request.POST.get('position')

    if request.FILES.get('image'):
        user_pic = request.FILES.get('image')
    else:
        user_pic = 'profile_pic/image.jpg'
    try:
        n = User.objects.get(user_email=email)
        # number already exists
        return render(request, 'users/add.html', { 'error_message': 'Already registered email :' + email})
    except ObjectDoesNotExist:
        user = User.objects.create(user_email=email, user_fname=fname, user_lname=lname, user_position=position, user_image=user_pic)
        user.save()
        return HttpResponseRedirect('/users')