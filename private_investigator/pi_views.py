from django.shortcuts import render , redirect
from django.http import HttpResponse
# from .forms import *
# from private_investigator.models import *
# from chat.models import Thread
# from django.core.files.storage import FileSystemStorage
# from django.core.files.storage import default_storage
# import cv2
# from django.http import JsonResponse
import requests
# from django.urls import reverse

# import random
# import string

# import PyPDF2
# import re
# import datetime

# import base64
# from io import BytesIO
# from PIL import Image

# from django.db import connections
# # Create your views here.
# from django.core import serializers
# from django.http import HttpResponse

all_url = "http://127.0.0.1:3000/"

def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post(all_url+"pi_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/pi_admin_dashboard/{uidd}")
        else:
            error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
        
    context = {'error':error}
    return render(request,"pi_signin.html",context)


def signup(request):
    error = ""
    if request.method == "POST":
        
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post(all_url+'pi_signup/',data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 302:
                   error = "User Already Exist"
                else:
                   return redirect(f"/pi_otpcheck/{uidd}")      
    context = {'error':error}
        
    return render(request,'pi_signup.html',context)

def opt_check(request,id):
    # form1 = ProfileOtpForm()
    # get = requests.get(f" http://127.0.0.1:3000/otp/{id}").json()
    # print(get['otp'])
    # print(get['uid'])
    context = {'invalid':"invalid"}
    new=[]
    if request.method == "POST":
        new.append(request.POST["otp1"])
        new.append(request.POST["otp2"])
        new.append(request.POST["otp3"])
        new.append(request.POST["otp4"])
        data = {
            'user_otp':int(''.join(new).strip())
           
        }
        print(data)
        # response = requests.post(f"http://54.159.186.219:8000/otp/{id}",   data=data)
        response = requests.post(f"http://127.0.0.1:3000/pi_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/pi_profilepicture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}

    return render(request,'pi_otpcheck.html',context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.POST)
        # response = requests.post(f"http://54.159.186.219:8000/profilepicture/{id}",files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/pi_profilePicture/{id}",files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/pi_complete_profile/{uidd}")
        # else:
            # return HttpResponse("INVALID data")
    return render(request,"pi_profilepicture.html")

def complete_profile(request,id):
    if request.method == "POST":
        print(request.POST)
        # response = requests.post(f"http://54.159.186.219:8000/profilepicture/{id}",files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/pi_complete_account/{id}",data = request.POST,files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/pi_admin_dashboard/{uidd}")
        # else:
            # return HttpResponse("INVALID data")
    return render(request,"uploadprofile.html")

def admin_dashboard(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        pf_users = requests.get("http://127.0.0.1:3000/alluserdata/").json()
        # print(pf_users)
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'profile_finder':pf_users,
                 }
        return render(request,"admin_dashboard.html",context)

def profile(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        print(my)
        context={'key':my,
                 'current_path':request.get_full_path()
                 }
        return render(request,"profile.html",context)

def edit_profile(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        print(my)
        context={'key':my,
                 'current_path':request.get_full_path()
                 }
        return render(request,"edit_profile.html",context)

def payment(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        print(my)
        context={'key':my,
                 'current_path':request.get_full_path()
                 }
        return render(request,"pi_payment1.html",context)

def client_list(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        # print(my)
        all_profinder_data = requests.get("http://127.0.0.1:3000/alluserdata/").json()
        if "client_one" in request.POST:
            print(request.POST)
            global client_one
            client_one = request.POST['client_one']
            return redirect(f"/pi_client_details/{id}")
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'all_profinder_data':all_profinder_data,
                 }
        return render(request,"Client_list.html",context)

def client_details(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        # print(my)
        client_list(request,id)
        print(client_one)
        all_profinder_data = requests.get("http://127.0.0.1:3000/alluserdata/").json()
        for x in all_profinder_data:
            if x['uid'] == client_one:
                specific_user = x
             
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'specific_user':[specific_user],
                 }
        return render(request,"client_details.html",context)


def subscription(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        print(my)
        context={'key':my,
                 'current_path':request.get_full_path()
                 }
        return render(request,"pi_subscription.html",context)

def payment_table(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        print(my)
        context={'key':my,
                 'current_path':request.get_full_path()
                 }
        return render(request,"pi_payment_table.html",context)


def add_client(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        # print(my)
        my_client = requests.get(f"http://127.0.0.1:3000/pi_my_clients/{id}").json()[id]
        # print(my_client)
        if "my_client_one" in request.POST:
           print(request.POST)
           global my_client_one
           my_client_one = request.POST['my_client_one']  
           return redirect(f"/pi_client_feedback/{id}")
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'my_client':my_client,
                 }
        return render(request,"pi_add_new_client.html",context)


def client_feedback(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        # print(my)
        add_client(request,id)
        print(my_client_one)
        all_profile_finder = requests.get("http://127.0.0.1:3000/alluserdata/").json()
        for x in all_profile_finder:
            if my_client_one == x['uid']:
                specific_user = x
                print(specific_user)

        
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'specific_user':[specific_user],
                 }
        return render(request,"pi_client_feedback.html",context)

def setting(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        print(my)
        context={'key':my,
                 'current_path':request.get_full_path()
                 }
        return render(request,"pi_Account_Settings.html",context)

