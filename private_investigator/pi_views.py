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
import json
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
    #hiring manager list
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    neww=[]
    response = requests.get('https://api.first.org/data/v1/countries').json()
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(all["data"])
    al = (all["data"])
    for x in al:
        name = (x.get("name"))
        neww.append(name)
    countryname = json.dumps(neww)

    context = {'response': response, 'region': response,'all':al,
                                            'country': countryname,'states': states,'hiring_manager':hiring_manager}

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
    return render(request,"uploadprofile.html",context)

def admin_dashboard(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        pf_users = requests.get("http://127.0.0.1:3000/alluserdata/").json()
        # print(pf_users)
        my_client = requests.get(f"http://127.0.0.1:3000/pi_my_clients/{id}").json()[id]
        filtered_clients = []
        for x in my_client:
            if "empty" not in x['answer']:
                filtered_clients.append(x)
        #closed investigation'
        closed=[]
        for x in my_client:
            # print(x['answer'])
            if x['answer'] is None:
                print("")
            elif "empty" not in x['answer']:
                closed.append("1")
        # print(len(closed))
        
        # pending investigation
        pending=[]
        for x in my_client:
            # print(x['answer'])
            if x['answer'] is None:
                pending.append("1")
            elif "empty" in x['answer']:
                pending.append("1")
        # print(len(pending))
        if len(filtered_clients) != 0:
            # percentage
            bad_review = []
            good_review=[]
            for j in filtered_clients:
                if j['rating'] == "empty":
                    bad_review.append(j['rating'])
                elif j['rating'] == "0":
                    bad_review.append(j['rating'])
                elif j['rating'] == "1.0":
                    bad_review.append(j['rating'])
                elif j['rating'] == "2.0":
                    bad_review.append(j['rating'])
                elif j['rating'] == "3.0":
                    good_review.append(j['rating'])
                elif j['rating'] == "4.0":
                    good_review.append(j['rating'])
                elif j['rating'] == "5.0":
                    good_review.append(j['rating'])
            badreview = int(len(bad_review)/len(filtered_clients)*100)
            goodreview = int(len(good_review)/len(filtered_clients)*100)
            
            #total ratings
            total_r = []
            one=[]
            two=[]
            three=[]
            four=[]
            five=[]
            
            for z in filtered_clients:
               print(z['rating'])
               if "empty" not in z['rating']:
                   total_r.append(z['rating'])
            print(total_r)
            
            for j in filtered_clients:
                if j['rating'] == "1.0":
                    one.append(j['rating'])
                elif j['rating'] == "2.0":
                    two.append(j['rating'])
                elif j['rating'] == "3.0":
                    three.append(j['rating'])
                elif j['rating'] == "4.0":
                    four.append(j['rating'])
                elif j['rating'] == "5.0":
                    five.append(j['rating'])
            score_total = len(five)*5 + len(four) * 4 + len(three) * 3 + len(two) * 2 + len(one) * 1
            response_total = len(five)+ len(four) + len(three) + len(two)+len(one)
            total_ratings = score_total/response_total
            print((total_ratings))
        else:
            total_ratings=0
            
    
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'profile_finder':pf_users,
                 'my':my,
                 'my_client':my_client,
                 'closed':len(closed),
                 'pending':len(pending),
                'total_ratings':total_ratings,
                'filtered_clients':filtered_clients,

                 }
        return render(request,"admin_dashboard.html",context)

def profile(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        # print(my)
        my_clients = requests.get(f"http://127.0.0.1:3000/pi_my_clients/{id}").json()[id]
        filtered_clients = []
        if len(my_clients) != 0:
            for x in my_clients:
                if "empty" not in x['answer']:
                    filtered_clients.append(x)
            if len(filtered_clients) != 0:
                # percentage
                bad_review = []
                good_review=[]
                for j in filtered_clients:
                    if j['rating'] == "empty":
                        bad_review.append(j['rating'])
                    elif j['rating'] == "0":
                        bad_review.append(j['rating'])
                    elif j['rating'] == "1.0":
                        bad_review.append(j['rating'])
                    elif j['rating'] == "2.0":
                        bad_review.append(j['rating'])
                    elif j['rating'] == "3.0":
                        good_review.append(j['rating'])
                    elif j['rating'] == "4.0":
                        good_review.append(j['rating'])
                    elif j['rating'] == "5.0":
                        good_review.append(j['rating'])
                badreview = int(len(bad_review)/len(filtered_clients)*100)
                goodreview = int(len(good_review)/len(filtered_clients)*100)
            
                print(len(bad_review))
                print(len(filtered_clients))
                print(badreview)
                print(goodreview)
           
                #total ratings
                total_r = []
                one=[]
                two=[]
                three=[]
                four=[]
                five=[]
                
                for z in filtered_clients:
                #    print(z['rating'])
                    if "empty" not in z['rating']:
                       total_r.append(z['rating'])
                # print(total_r)
                
                       for j in filtered_clients:
                           print(j['rating'])
                           if j['rating'] == "1.0":
                               one.append(j['rating'])
                           elif j['rating'] == "2.0":
                               two.append(j['rating'])
                           elif j['rating'] == "3.0":
                               three.append(j['rating'])
                           elif j['rating'] == "4.0":
                               four.append(j['rating'])
                           elif j['rating'] == "5.0":
                               five.append(j['rating'])
                       score_total = len(five)*5 + len(four) * 4 + len(three) * 3 + len(two) * 2 + len(one) * 1
                       response_total = len(five)+ len(four) + len(three) + len(two)+len(one)
                       total_ratings = score_total/response_total
                    else:
                        total_ratings=0
            else:
                badreview=0
                goodreview=0
                total_ratings=0
        else:
            badreview=0
            goodreview=0
            total_ratings=0
        print(total_ratings)
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'my_clients':filtered_clients,
                 'bad_review':badreview,
                 'good_review':goodreview,
                 'total_ratings':total_ratings,
                 }
        return render(request,"profile.html",context)

def edit_profile(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        # print(my)
        if request.method == "POST":
            print(request.POST)
            print(request.FILES)
            response = requests.post(f"http://127.0.0.1:3000/pi_edit_account/{id}",data=request.POST,files=request.FILES)
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
        
        my_client = requests.get(f"http://127.0.0.1:3000/pi_my_clients/{id}").json()[id]
        if len(my_client) == 0:
            all_profinder_data_values = requests.get("http://127.0.0.1:3000/alluserdata/").json()
        else:
            all_profinder_data_values=[]
            all_profinder_data = requests.get("http://127.0.0.1:3000/alluserdata/").json()
            for x in all_profinder_data:
                if x['uid'] not in str(my_client):
                    print(x)
                    all_profinder_data_values.append(x)

        #post
        if "client_one" in request.POST:
            print(request.POST)
            global client_one
            client_one = request.POST['client_one']
            return redirect(f"/pi_client_details/{id}")
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'all_profinder_data':all_profinder_data_values,
                 'my_client':my_client,
                 }
        return render(request,"Client_list.html",context)

def client_details(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        jsonDec = json.decoder.JSONDecoder()
        # print(my)
        client_list(request,id)
        print(client_one)
        all_profinder_data = requests.get("http://127.0.0.1:3000/alluserdata/").json()
        for x in all_profinder_data:
            if x['uid'] == client_one:
                specific_user = x
                if specific_user['Questin'] is not None:
                   question = jsonDec.decode(specific_user['Questin'])
                   print(question)
                else:
                    question=""
                # question_and_Answer = requests.get(f"http://127.0.0.1:3000/my_question_and_answer/{x['uid']}").json()[x['uid']]
             
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'specific_user':[specific_user],
                 'question_and_Answer':question,
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
        # print(my_client[0]['answer'])
        if len(my_client) !=0:
            if "empty" not in str(my_client[0]['answer']):
                result= "complete"
            else:
                result= "empty"
        else:
            result="empty"
        if "my_client_one" in request.POST:
           print(request.POST)
           global my_client_one
           my_client_one = request.POST['my_client_one']  
           return redirect(f"/pi_client_feedback/{id}")
        context={'key':my,
                 'current_path':request.get_full_path(),
                 'my_client':my_client,
                'result' :result,

                 }
        return render(request,"pi_add_new_client.html",context)


def client_feedback(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        # print(my)
        # add_client(request,id)
        # print(my_client_one)
        profile_finder_value = requests.get(f"http://127.0.0.1:3000/pi_my_clients/{id}").json()[id]
        
        # print(all_profile_finder)
        for x in profile_finder_value:
            if my_client_one == x['uid']:
                print(x)
                specific_user = x
                print( x['Questin'])
                all_profile_finder_Questin = x['Questin']
                all_profile_finder_answer = x['answer']
                all_profile_finder = zip(all_profile_finder_Questin,all_profile_finder_answer)
                # question_and_Answer = requests.get(f"http://127.0.0.1:3000/my_question_and_answer/{x['uid']}").json()[x['uid']]
                # situation_prediction = requests.get(f"http://127.0.0.1:3000/my_question_and_answer/{x['uid']}").json()[x['uid']]
                question_and_Answer = x
                situation_prediction = x
                # print(question_and_Answer)
                if "empty" not in str(question_and_Answer):
                    result= "complete"
                else:
                    result = "empty"
        
        #situation
        print("situation")
        # sit = []
        # for x in situation_prediction:
        #     sit.append(x['answer'])
        # if "empty" in sit:
        #     situation = "pending"
        # else:
        #     situation = "complete"
              
        #post
        if request.method=="POST":
            print(request.POST)
            data={
                'answer':request.POST['answer'],
                'question':request.POST['question'],
                'my_investigator':id
            }
            response = requests.post(f"http://127.0.0.1:3000/my_question_and_answer/{specific_user['uid']}",data=data)
            print(response)
            print(response.status_code)
            print(response.text)

        context={'key':my,
                 'current_path':request.get_full_path(),
                 'specific_user':[specific_user],
                 'question_and_Answer':question_and_Answer,
                 'result' :result,
                 'all_profile_finder':all_profile_finder,
                #  'situation':situation,
                 }
        return render(request,"pi_client_feedback.html",context)

def setting(request,id):
        my = requests.get(f"http://127.0.0.1:3000/pi_my_data/{id}").json()[0]
        print(my)
        context={'key':my,
                 'current_path':request.get_full_path()
                 }
        return render(request,"pi_Account_Settings.html",context)

