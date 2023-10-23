from django.shortcuts import render , redirect
from django.http import HttpResponse
# from .forms import *
# from .models import *
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
# Create your views here.
# from django.core import serializers
# from django.http import HttpResponse
all_url = "http://127.0.0.1:3000/"
# all_url = "http://18.205.163.238/"
def mainpage(request):
    return render(request,'mainpage.html')
def signin(request):
    # current_path =  request.get_full_path()
    # print(current_path)
    # form1 = ProfileSigninForm()
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post(all_url+"signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/profile_page/{uidd}")
        else:
            error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
            # form = ProfileSigninForm(request.POST)
        #print("hello")
        #  if form.is_valid():
        #     email = request.POST['email']
        #     password = request.POST['password']
        #     mydata = profile_finder.objects.filter(email=email).filter(password=password).values() 
        #     mydatalen = len(mydata)
        #     if mydatalen == 1:
        #         request.session['email'] = email
        #         return redirect('/profile_page') 
    context = {'error':error}
    return render(request,"signin.html",context)


def signup(request):
    # form1 = ProfileFinderForm()
    error = ""
    if request.method == "POST":
        
        if request.POST['password'] == request.POST['confirm_password']:
            if len(request.POST['referral_code']) == "0":
                data = {
            "email":request.POST["email"],
            "mobile" : request.POST["mobile"],
            "password":request.POST["password"],
            "referal_code" : "no referal code",
        }
                # response = requests.post('http://54.159.186.219:8000/signup/',data=data)
                response = requests.post(all_url+'signup/',data=data)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 302:
                   error = "User Already Exist"
                else:
                   return redirect(f"/otp/{uidd}")
               
               
            else:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post(all_url+'signup/',data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 302:
                   error = "User Already Exist"
                else:
                   return redirect(f"/otp/{uidd}")
                
    context = {'error':error}

        # code = ""
        # if str(request.POST['referal_code']).strip() == " ":
        #     code = "empty"
        # else:
        #     code = request.POST['referal_code']
        # data = {
        #     "email":request.POST["email"],
        #     "mobile" : request.POST["mobile"],
        #     "password":request.POST["password"],
        #     "referal_code" : code
        # }
        # print(data)
        # response = requests.post("http://127.0.0.1:8000/signup/", data=request.POST)
        # print(response.status_code)
        # aa = response.text
        # # .split("\"")[1]
        # print(aa)
        # if response.status_code == 302:
        #       return redirect("/")
        # elif response.status_code == 200:
        #       return redirect("/otp/{}".format(aa))
        # form = ProfileFinderForm(request.POST)
        # print("hello")
        # if form.is_valid():
        #     print("hello2")
        #     allowed_chars = ''.join((string.ascii_letters, string.digits))
        #     unique_id = ''.join(random.choice(allowed_chars) for _ in range(6))
        #     code = unique_id
        #     otp = random.randrange(100000, 1000000)
        #     email = form.cleaned_data['email']
        #     mobile = form.cleaned_data['mobile']
        #     password = form.cleaned_data['password']
        #     confirm_password = form.cleaned_data['confirm_password']
        #     referral_code = form.cleaned_data['referral_code']
        #     mydata = profile_finder.objects.filter(email=email).values() 
        #     mydatalen = len(mydata)
        #     print(email)
        #     print(mobile)
        #     print(password)
        #     print(confirm_password)
        #     print(referral_code)
        #     print(code)
        #     print(otp)
        #     if mydatalen == 0:
        #         profile_finder.objects.create(
        #             email=email,
        #             mobile=mobile,
        #             password=password,
        #             confirm_password=confirm_password,
        #             referral_code=referral_code,
        #             code=code,
        #             user_otp = otp,
        #         )
        #         request.session['email'] = email
        #         return redirect('/otp')
        #     else:
        #         return render(request,'signup.html',{'form':form1})
        #     #form.save()
        
    return render(request,'signup.html',context)#{'form':form1})


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
        response = requests.post(f"http://127.0.0.1:3000/otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/profileforwhom/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    
    
        # else:
        #                 return redirect("/profile_page")
        #form = ProfileFinderForm()
        # form = ProfileOtpForm(request.POST)
        # print("hello")
        # if form.is_valid():
        #     #print("HAI")
            
        #     #user_otp = form.cleaned_data['user_otp']
        #     user_otpli = request.POST.getlist('user_otp[]')
        #     user_otp0=[str(i) for i in user_otpli]
        #     user_otp = "".join(user_otp0)
        #     print(user_otp)
        #     #print("".join(s))
        #     profile_finder_email=request.session['email']
        #     mydata = profile_finder.objects.filter(email=profile_finder_email).filter(user_otp=user_otp).values() 
        #     mydatalen = len(mydata)
        #     if mydatalen == 1:
        #         return redirect('/dashboard')
        #     else:
        #         return render(request,'otpcheck.html',{'form':form1})

    return render(request,'otpcheck.html',context)

# def profile_dashboard(request,id):
#     my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
#     context={'key':my}
#     return render(request,'dashboard.html',context)
def profile_dashboard(request):
    # my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    # context={'key':my}
    return render(request,'dashboard.html')

def profileidcard(request,id):
    # saved = False
    # if request.method == "POST":
    #     form = profileIdCardForm(request.POST,request.FILES)
    #     print("hello")
    #     if form.is_valid():
    #         myfile = request.FILES['idcard']
    #         fs = FileSystemStorage()
    #         fs.location = fs.location+'/pictures/'
    #         #print(fs.location)
    #         filename = fs.save(myfile.name, myfile)
    #         uploaded_file_url = fs.url(filename)
    #         x = uploaded_file_url.split('/')
    #         #print(x[1])
    #         id_url = x[1]+"/pictures/"+x[2]
    #         pdf_file = open(id_url, 'rb')
    #         pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    #         string = []
    #         phda=0
    #         data =[]
    #         for page_num in range(pdf_reader.numPages):
    #             page = pdf_reader.getPage(page_num)
    #             #print(page)
    #             lines = page.extractText().splitlines()
    #             for line in lines:
    #                 string.append(re.sub(r'[^a-zA-Z0-9-/: ]', '', line))
    #                 #print(line)


    #         for i in string:
    #             if i.strip() != '':
    #                 data.append(i)


    #         for a in data:
    #             if a.isdigit() and len(a) == 10:
    #                 #print(a)
    #                 phda = data.index(a)
                

    #         # if  data[9].isdigit():
    #         #     phone = data[9]
    #         #     aadhar = data[10]
    #         # else:
    #         #     phone = data[10]
    #         #     aadhar = data[11]
    #         if len(data) > 1:
    #             name = data[2]
    #             father_name = data[3].split(" ")[1].strip()
    #             address = data[4]+"\n"+data[5]+"\n"+data[6]+"\n"+data[7]
    #             phone = data[phda]
    #             aadhar = data[phda+1]
    #             dob = data[phda+9].split(":")[1].strip()
    #             gender = data[phda+10].split("/")[1].strip()
    #             district = data[-7].split("-")[0].strip()
    #             pincode = data[-7].split("-")[1].strip()

    #             print("Name :",name)
    #             print("Father Name :",father_name)
    #             print("Address : ",address)
    #             print("Phone : ",phone)
    #             print("Aadhar : ",aadhar)
    #             print("Dob : ",dob)
    #             print("Gender : ",gender)
    #             print("District :",district)
    #             print("Pincode :",pincode)
    #             profile_finder_email=request.session['email']
    #             profile_finder.objects.filter(email=profile_finder_email).update(idcard=id_url ,
    #             name=name,family_fathername=father_name,address=address,primary_phone=phone,aadhar=aadhar,
    #             dob=dob,gender=gender,district=district,pincode=pincode)
    #             saved = True
    #             return redirect('/profileforwhom')

    #         else:
    #             print("Enter Correct PDF Format")
    #             return render(request,'profileidcard.html',locals())
            
        
    # return render(request,'profileidcard.html',locals())
    # a= requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    # print(a)
    context={
        'key':id
    }
    if request.method == "POST":
        print(request.POST)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/profileidcard/{id}",   files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/profileform/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,'profileidcard.html',context)
    



def profileforwhom(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    mydata=[my]
    context = {
            'key':id,
           
               }
    return render(request,'profileforwho.html',context)

def profile_manager_list(request,id):
    context = {
            'key':id,
           
               }
    return render(request,'profile-man-list.html',context)

def private_investigator_list(request,id):
    pi_data = requests.get(f"http://127.0.0.1:3000/all_private_investigator_data").json()

    if request.method == "POST":
        print(request.POST)
        data={
            'pf_id':id,
            'pi_id':request.POST['hire']
        }
        response = requests.post(f"http://127.0.0.1:3000/pi_my_clients/{id}",   data=data)
        response = requests.post(f"http://127.0.0.1:3000/my_investigator/{id}",   data=data)
        print(response)
        print(response.status_code)
        print(response.text)
    context = {
            'key':id,
            'pi_data':pi_data,
           
               }
    return render(request,'private_investigator_list.html',context)



def profileform(request,id):
    
    # current_url = request.build_absolute_uri
    # absolute_url = request.build_absolute_uri(current_url)
    # #print(absolute_url)
    # x = absolute_url.split("?")
    # pa = x[1].split("'")
    # profileforwho = pa[0]
    # print(profileforwho)
    # profile_finder_email = request.session['email']
    # if pa[0]=="myself":
    #     da = profile_finder.objects.filter(email=profile_finder_email).values()
    # else:
    #     da=""
    # coun = countries.objects.all()
    # #print(coun)
    # #context = {'countries': countries}
    # if 'email' not in request.session:
    #     return HttpResponse("Email not found in session.")
    
    # profile_finder_email = request.session['email']
    # print(profile_finder_email)
    # form = profileForm(request.POST, request.FILES)
    # if request.method == "POST":
        
    #     print("djfhjsdh")
    #     # print(form.is_valid())
    #     if form.is_valid():
    #         print("trtrt")
    #         #cd = form.cleaned_data
            
    #         height = request.POST['height']
            
    #         weight = request.POST['weight']
    #         print(height)
    #         print(weight)
    #         martial = request.POST['martial']
    #         physical = request.POST['physical']
    #         birth_place = request.POST['birth_place']
            
    #         birth_country = request.POST['birth_country']
    #         print(martial)
    #         print(physical)
    #         print(birth_place)
    #         print(birth_country) 
            
    #         birth_time = request.POST['birth_time']
            
    #         birth_city = request.POST['birth_city']
            
    #         orgin = request.POST['orgin']
            
    #         r_country = request.POST['r_country']
    #         print(birth_time)
    #         print(birth_city)
    #         print(orgin)
    #         print(r_country) 
    #         r_state = request.POST['r_state']
    #         denomination = request.POST['denomination']
    #         blood_group = request.POST['blood_group']
    #         r_status = request.POST['r_status']
    #         print(r_state)
    #         print(denomination)
    #         print(blood_group)
    #         print(r_status) 
    #         #print(city)
    #         temple_name = request.POST['temple_name']
    #         street = request.POST['street']
    #         post_code = request.POST['post_code']
    #         country = request.POST['country']
    #         city = request.POST['city']
    #         print(temple_name)
    #         print(street)
    #         print(post_code)
    #         print(country) 
    #         print(city)
    #         address_phone = request.POST['address_phone']
    #         diocese = request.POST['diocese']
    #         local_admin = request.POST['local_admin']
    #         emergency_name = request.POST['emergency_name']
    #         relation = request.POST['relation']
    #         #print(relation)
    #         print(address_phone)
    #         print(diocese)
    #         print(local_admin)
    #         print(emergency_name) 
    #         print(relation)
    #         #print(emergency_name1)
    #         emergency_number = request.POST['emergency_number']
    #         emergency_email = request.POST['emergency_email']
    #         emergency_martial = request.POST['emergency_martial']
    #         emergency_occupation = request.POST['emergency_occupation']
    #         emergency_name1 = request.POST['emergency_name1']
    #         #print(relation1)
    #         print(emergency_number)
    #         print(emergency_email)
    #         print(emergency_martial) 
    #         print(emergency_occupation)
    #         print(emergency_name1)
    #         relation1 = request.POST['relation1']
    #         emergency_number11 = request.POST['emergency_number1']
    #         if len(emergency_number11) == 0:
    #             emergency_number1 = 0
    #         else:
    #             emergency_number1 = emergency_number11
    #         emergency_email1 = request.POST['emergency_email1']
    #         emergency_martial1= request.POST['emergency_martial1']
    #         emergency_occupation1 = request.POST['emergency_occupation1']
    #         dob = request.POST['dob']
    #         # print(dob)
    #         # y = dob.year
    #         # current_year = datetime.datetime.now().year
    #         # age = current_year-y
    #         print(relation1)
    #         print(emergency_number1)
    #         print(emergency_email1)
    #         print(emergency_martial1) 
    #         print(emergency_occupation1)
    #         if len(request.FILES) != 0:

    #             myfile = request.FILES['upload_idcard']
    #             fs = FileSystemStorage()
    #             fs.location = fs.location+'/profileid/'
    #             filename = fs.save(myfile.name, myfile)
    #             uploaded_file_url = fs.url(filename)
    #             x = uploaded_file_url.split('/')
    #             upload_id = x[1]+"/profileid/"+x[2]
    #             print(upload_id)
    #             pdf_file = open(upload_id, 'rb')
    #             pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    #             string = []
    #             phda=0
    #             data =[]
    #             for page_num in range(pdf_reader.numPages):
    #                 page = pdf_reader.getPage(page_num)
    #                 #print(page)
    #                 lines = page.extractText().splitlines()
    #                 for line in lines:
    #                     string.append(re.sub(r'[^a-zA-Z0-9-/: ]', '', line))
    #                     #print(line)


    #             for i in string:
    #                 if i.strip() != '':
    #                     data.append(i)


    #             for a in data:
    #                 if a.isdigit() and len(a) == 10:
    #                     #print(a)
    #                     phda = data.index(a)
                    

    #             # if  data[9].isdigit():
    #             #     phone = data[9]
    #             #     aadhar = data[10]
    #             # else:
    #             #     phone = data[10]
    #             #     aadhar = data[11]
    #             if len(data) > 1:
    #                 nameo = data[2]
    #                 father_nameo = data[3].split(" ")[1].strip()
    #                 addresso = data[4]+"\n"+data[5]+"\n"+data[6]+"\n"+data[7]
    #                 phoneo = data[phda]
    #                 aadharo = data[phda+1]
    #                 dobo = data[phda+9].split(":")[1].strip()
    #                 gendero = data[phda+10].split("/")[1].strip()
    #                 districto = data[-7].split("-")[0].strip()
    #                 pincodeo = data[-7].split("-")[1].strip()

    #                 print("Name :",nameo)
    #                 print("Father Name :",father_nameo)
    #                 print("Address : ",addresso)
    #                 print("Phone : ",phoneo)
    #                 print("Aadhar : ",aadharo)
    #                 print("Dob : ",dobo)
    #                 print("Gender : ",gendero)
    #                 print("District :",districto)
    #                 print("Pincode :",pincodeo)
    #             else:
    #                 print("Enter Correct PDF Format")
    #         else:
    #             upload_id = ""
    #             nameo = ""
    #             father_nameo = ""
    #             addresso = ""
    #             phoneo = ""
    #             aadharo = ""
    #             dobo = ""
    #             gendero = ""
    #             districto = ""
    #             pincodeo = ""
    #         profile_finder.objects.filter(email=profile_finder_email).update(
    #             height=height, weight=weight, martial=martial, physical=physical,
    #             birth_place=birth_place, birth_country=birth_country, birth_time=birth_time,
    #             birth_city=birth_city, orgin=orgin, r_country=r_country, r_state=r_state,
    #             denomination=denomination, blood_group=blood_group, r_status=r_status,
    #             temple_name=temple_name, street=street, post_code=post_code, country=country,
    #             city=city, address_phone=address_phone, diocese=diocese, local_admin=local_admin,
    #             emergency_name=emergency_name, relation=relation, emergency_number=emergency_number,
    #             emergency_martial=emergency_martial, emergency_email=emergency_email,
    #             emergency_occupation=emergency_occupation, emergency_name1=emergency_name1,
    #             relation1=relation1, emergency_number1=emergency_number1,
    #             emergency_martial1=emergency_martial1, emergency_email1=emergency_email1,
    #             emergency_occupation1=emergency_occupation1,upload_idcard=upload_id,dob=dob,
    #             nameo=nameo,father_nameo=father_nameo,addresso=addresso,dobo=dobo,gendero=gendero,
    #             districto=districto,pincodeo=pincodeo,profileforwho=profileforwho,aadharo=aadharo
    #         )

    #         return redirect('/selfie_upload')
            
    # # else:
    # #     form = profileForm()

    # return render(request, 'profileform.html', {'form':form , 'countries':coun , 'da':da})
    import json
    neww = []
    response = requests.get('https://api.first.org/data/v1/countries').json()
    region = (requests.get('https://api.first.org/data/v1/countries').json())
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(statess["data"])

    al = (all["data"])

    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)
    context = {'response': response, 'region': region,'all':al,
                                           'country': countryname,'states': states}
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        data={
            'name':request.POST['name'],
            'address':request.POST['address'],
            'height':request.POST['height'],
            'weight':request.POST['weight'],
            'gender':request.POST['gender'],
            'marital':request.POST['marital'],
            'physical':request.POST['physical'],
            'religion':request.POST['religion'],
            'age':request.POST['age'],
            'birth_place':request.POST['birth_place'],     
            'birth_country':request.POST['birth_country'],   
            'birth_time':request.POST['birth_time'],
            'birth_city':request.POST['birth_city'],
            'origin':request.POST['origin'],
            'r_country':request.POST['r_country'],
            'r_state':request.POST['r_state'],
            'r_status':request.POST['r_status'],
            'denomination':request.POST['denomination'],
            'blood_group':request.POST['blood_group'],
            'temple_name':request.POST['temple_name'],
            'temple_street':request.POST['temple_street'],
            'temple_post_code':request.POST['temple_post_code'],
            'temple_country':request.POST['temple_country'],
            'temple_city':request.POST['temple_city'],
            'temple_phone_number':request.POST['temple_phone_number'],
            'temple_diocese':request.POST['temple_diocese'],
            'temple_local_admin':request.POST['temple_local_admin'],
            'emergency_name':request.POST.getlist('emergency_name'),
            'emergency_relation':request.POST.getlist('emergency_relation'),
            'emergency_phone_number':request.POST.getlist('emergency_phone_number'),
            'emergency_email':request.POST.getlist('emergency_email'),
            'emergency_marital_status':request.POST.getlist('emergency_marital_status'),
            'emergency_occupations':request.POST.getlist('emergency_occupations')

        }
        # response = requests.post(f"http://54.159.186.219:8000/profileform/{id}", data=request.POST,files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/profileform/{id}", data=data,files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/selfie_upload/{uidd}")
        else:
            pass
    return render(request, 'profileform.html',context)


def statelist(request , pk):
    import json
    #print(pk)
    stateli = list(states.objects.filter(country_id=pk).values())
    #print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)


def rstatelist(request , pk):
    import json
    # print(pk)
    stateli = list(states.objects.filter(country_id=pk).values())
    # print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)


def fstatelist(request , pk):
    import json
    # print(pk)
    stateli = list(states.objects.filter(country_id=pk).values())
    # print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)



def mstatelist(request , pk):
    import json
    # print(pk)
    stateli = list(states.objects.filter(country_id=pk).values())
    # print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)


def ccstatelist(request , pk):
    import json
    # print(pk)
    stateli = list(states.objects.filter(country_id=pk).values())
    # print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)

def citylist(request , pk):
    import json
    # print(pk)
    stateli = list(cities.objects.filter(state_id=pk).values())
    # print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)


def rcitylist(request , pk):
    import json
    # print(pk)
    stateli = list(cities.objects.filter(state_id=pk).values())
    # print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)



def citylistp(request , pk):
    import json
    # print(pk)
    stateli = list(states.objects.filter(country_id=pk).values())
    # print(stateli)
    data_json = json.dumps(stateli)
    #return render(request, 'profileform.html', {'states':data_json})
    return JsonResponse(data_json, safe=False)

def selfie_upload(request,id):
   
    # if request.method == "POST":
    #     profile_finder_email = request.session['email']
    #     form = profilepictureForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         code = profile_finder.objects.filter(email=profile_finder_email).values()
    #         #print(code[0]['code'])
    #         imgname="media/profile_picture/"+str(code[0]['code'])+str(code[0]['referral_code'])+".png"
    #         print(imgname)
    #         b64_string = request.POST['profile_picture']
    #         data = base64.b64decode(b64_string.split(",")[1])
    #         img = Image.open(BytesIO(data))
    #         img.save(imgname)
    #         profile_finder.objects.filter(email=profile_finder_email).update(
    #             profile_picture=imgname
    #         )
    #         return redirect('/primary_details')
    context = {
    'key':id,
           }

    if request.method == "POST":
        print(request.POST)
        # response = requests.post(f"http://54.159.186.219:8000/profilepicture/{id}",files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/profilepicture/{id}",files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/primary_details/{uidd}")
        # else:
            # return HttpResponse("INVALID data")
    return render(request,"profilepicture.html",context)

#primary details options 


def primary_details(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    mydata = [my]
    profile_pic = mydata[0]['profile_picture']

    import json
    neww = []
    response = requests.get('https://api.first.org/data/v1/countries').json()
    region = (requests.get('https://api.first.org/data/v1/countries').json())
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(statess["data"])

    al = (all["data"])

    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)
    context = {'response': response, 'region': region,'all':al,
                                           'country': countryname,'states': states,'profile_pic':profile_pic}
                                           
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # new=[]
        # a=  request.FILES.getlist('gallery')
        # # print(data["your_intrest"])
        # # print(files["selfie"])
        # for x in a:
        #   b=str(x)
        #   new.append(b)
        # ss = str(new)
        data = {
            'marital_status': request.POST['marital_status'],
            'physical_mental_status': request.POST['physical_mental_status'],
            'primary_email': request.POST['primary_email'],
            'primary_phone_number': request.POST['primary_phone_number'],
            'dob': request.POST['dob'],
            'why_marry': request.POST['why_marry'],
            'behind_decision': request.POST['behind_decision'],
            'education_school': request.POST.getlist('education_school'),
            'education_year': request.POST.getlist('education_year'),
            'education_course': request.POST.getlist('education_course'),
            'education_major': request.POST.getlist('education_major'),
            'are_you_working_now': request.POST.getlist('are_you_working_now'),
            'company_name': request.POST.getlist('company_name'),
            'position': request.POST.getlist('position'),
            'profession': request.POST.getlist('profession'),
            'salary_range': request.POST.getlist('salary_range'),
            'your_intrest': request.POST.getlist('your_intrest'),
            'non_intrest': request.POST.getlist('non_intrest'),
            'complexion': request.POST.getlist('complexion'),
            'food_taste': request.POST.getlist('food_taste'),
            'daily_diet_plan': request.POST.getlist('daily_diet_plan'),
            'carriying_after_marriage': request.POST['carriying_after_marriage'],
            'tobacco': request.POST['tobacco'],
            'alcohol': request.POST['alcohol'],
            'drugs': request.POST['drugs'],
            'criminal_offence': request.POST['criminal_offence'],
            'primary_country': request.POST['primary_country'],
            'profile_tag': request.POST['profile_tag'],
            'treet_mypartner': request.POST['treet_mypartner'],
            'treet_their_side': request.POST['treet_their_side'],
            'orphan': request.POST['orphan'],
            'disable': request.POST['disable'],
            'whichorgan': request.POST['whichorgan'],
        }
        # print(type(data['behind_decision']))
        # print(type(data['education_school']))
        if "horoscope" not in request.FILES:
            horoscope = "empty"
        else:
            horoscope = request.FILES['horoscope']
        # image_paths = request.FILES.getlist('gallery')
        aa = request.FILES.getlist('gallery')
        files = {
            'selfie':request.FILES['selfie'],
            'full_size_image':request.FILES['full_size_image'],
            'family_image':request.FILES['family_image'],
            'horoscope':horoscope,
        }
        print(files)
        for i, file_data in enumerate(aa):
            files[f'file_{i}'] = file_data
        print(data)
        # print(files)
        # response = requests.post(f"http://54.159.186.219:8000/primarydetails/{id}",data = request.POST ,files=files)
        response = requests.post(f"http://127.0.0.1:3000/primarydetails/{id}",data =data ,files=files)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/family_details/{uidd}")
        else:
            # return HttpResponse("INVALID data")
            pass
    return render(request,"primary_details.html",context)

def family_details(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    mydata = [my]
    profile_pic = mydata[0]['profile_picture']

    import json
    neww = []
    response = requests.get('https://api.first.org/data/v1/countries').json()
    region = (requests.get('https://api.first.org/data/v1/countries').json())
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(statess["data"])

    al = (all["data"])

    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)
    context = {'response': response, 'region': region,'all':al,
                                           'country': countryname,'states': states,'profile_pic':profile_pic}
    if request.method == "POST":
        print(request.POST)
        data={
     'family_status': request.POST['family_status'],
            'father_name': request.POST['father_name'],
            'father_country': request.POST['father_country'],
            'father_city': request.POST['father_city'],
            'father_job': request.POST['father_job'],
            'father_family_name': request.POST['father_family_name'],
            'mother_name': request.POST['mother_name'],
            'mother_country': request.POST['mother_country'],
            'mother_city': request.POST['mother_city'],
            'mother_job': request.POST['mother_job'],
            'mother_family_name': request.POST['mother_family_name'],
            # 'sibling_name': str(request.POST.getlist('sibling_name')),
            # 'sibling_relation': str(request.POST.getlist('sibling_relation')),
            # 'sibling_young_or_old': str(request.POST.getlist('sibling_young_or_old')),
            # 'sibling_occupation': str(request.POST.getlist('sibling_occupation')),
            # 'sibling_marital': str(request.POST.getlist('sibling_marital')),
            # 'sibling_email': str(request.POST.getlist('sibling_email')),
            # 'sibling_dob': str(request.POST.getlist('sibling_dob')),
          
            'sibling_name': request.POST.getlist('sibling_name'),
            'sibling_relation': request.POST.getlist('sibling_relation'),
            'sibling_young_or_old': request.POST.getlist('sibling_young_or_old'),
            'sibling_occupation': request.POST.getlist('sibling_occupation'),
            'sibling_marital': request.POST.getlist('sibling_marital'),
            'sibling_email': request.POST.getlist('sibling_email'),
            'sibling_dob': request.POST.getlist('sibling_dob'),
    
            'about_candidate': request.POST['about_candidate'],
            'current_status': request.POST['current_status'],
        }
        print(type(data["sibling_name"]))
        print(data["sibling_name"])
        print(type(data["current_status"]))
        # response = requests.post(f"http://54.159.186.219:8000/familydetails/{id}",data = data)
        response = requests.post(f"http://127.0.0.1:3000/familydetails/{id}",data = data)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/contact_details/{uidd}")
        else:
            return HttpResponse("INVALID data")
    return render(request,"family_details.html",context)


def contact_details(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    mydata = [my]
    profile_pic = mydata[0]['profile_picture']

    import json
    neww = []
    response = requests.get('https://api.first.org/data/v1/countries').json()
    region = (requests.get('https://api.first.org/data/v1/countries').json())
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(statess["data"])

    al = (all["data"])

    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)
    context = {'response': response, 'region': region,'all':al,
    'country': countryname,'states': states,'profile_pic':profile_pic}
    if request.method == "POST":
        print(request.POST)
        if "contact_father_city" not in request.FILES:
            contact_father_city = "empty"
        else:
            contact_father_city = request.FILES['contact_father_city']
        #facebook
        if request.POST['facebook'] == "":
            facebook = "empty"
        else:
            facebook = request.FILES['facebook']
        print(facebook)
        #linkedin
        if request.POST['linkedin'] == "":
            linkedin = "empty"
        else:
            linkedin = request.FILES['linkedin']
        print(linkedin)
        #instagram
        if request.POST['instagram'] == "":
            instagram = "empty"
        else:
            instagram = request.FILES['instagram']
        print(instagram)
        #youtube
        if request.POST['youtube'] == "":
            youtube = "empty"
        else:
            youtube = request.FILES['youtube']
        print(youtube)
        #twitter
        if request.POST['twitter'] == "":
            twitter = "empty"
        else:
            twitter = request.FILES['twitter']
        print(twitter)
        #website
        if request.POST['website'] == "":
            website = "empty"
        else:
            website = request.FILES['website']
        print(website)
        data={
     'contact_father_name': request.POST['contact_father_name'],
            'contact_father_street': request.POST['contact_father_street'],
            'contact_father_zipcode': request.POST['contact_father_zipcode'],
            'contact_father_country': request.POST['contact_father_country'],
            'contact_father_city': contact_father_city,
            'contact_father_housename': request.POST['contact_father_housename'],
            'contact_mother_housename': request.POST['contact_mother_housename'],
            'contact_email': request.POST['contact_email'],
            'contact_phone': request.POST['contact_phone'],

            'whatsapp': request.POST['whatsapp'],
            'facebook': facebook,
            'linkedin': linkedin,
            'instagram': instagram,
            'youtube': youtube,
            'twitter': twitter,
            'website': website
        }
        print(data)
        # response = requests.post(f"http://54.159.186.219:8000/contactdetails/{id}",data = request.POST)
        response = requests.post(f"http://127.0.0.1:3000/contactdetails/{id}",data = data)
        # print(response)
        # print(response.status_code)
        # print(response.text)
        uidd = (response.text[1:-1])
        # print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/profile_page/{uidd}")
        else:
            return HttpResponse("INVALID data")
    return render(request,"contact_details.html",context)



def header(request):
  
    return render(request,'header.html')


def profile_page(request,id):
    # profile_finder_email=request.session['email']
    # print(profile_finder_email)
    # mydata = profile_finder.objects.filter(email=profile_finder_email).values() 
    #mydatalen = len(mydata)
    # my = requests.get(f"http://54.211.84.169:8000/alldata/{id}").json()
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    # print(my)
    mydata = [my]
    # print(mydata)
    profile_pic = mydata[0]['profile_picture']
    # profile_pic = mydata['id_card_1']
#sibling details
    sibling_name_value=[]
    sibling_relation_value=[]
    sibling_occupation_value=[]
    sibling_name = my['sibling_name'][1:-1].split(", ")
    sibling_relation = my['sibling_relation'][1:-1].split(", ")
    sibling_occupation = my['sibling_occupation'][1:-1].split(", ")
    for sibling_name_x in sibling_name:
        sibling_name_value.append(sibling_name_x[1:-1])
    for sibling_relation_x in sibling_relation:
        sibling_relation_value.append(sibling_relation_x[1:-1])
    for sibling_occupation_x in sibling_occupation:
        sibling_occupation_value.append(sibling_occupation_x[1:-1])
    sibling={}
    sib = [sibling]
    for i, sibling_name_data in enumerate(sibling_name_value):
            sibling[f'sibling_name_{i}'] = sibling_name_data
    for i, sibling_relation_data in enumerate(sibling_relation_value):
            sibling[f'sibling_relation_{i}'] = sibling_relation_data
    for i, sibling_occupation_data in enumerate(sibling_occupation_value):
            sibling[f'sibling_occupation_{i}'] = sibling_occupation_data
    
    # print(sib)

#education
    education_school_value=[]
    education_year_value=[]
    education_course_value=[]
    education_school = my['education_school'][1:-1].split(", ")
    education_year = my['education_year'][1:-1].split(", ")
    education_course = my['education_course'][1:-1].split(", ")
    for education_school_x in education_school:
        education_school_value.append(education_school_x[1:-1])
    for education_year_x in education_year:
        education_year_value.append(education_year_x[1:-1])
    for education_course_x in education_course:
        education_course_value.append(education_course_x[1:-1])
    education={}
    edu = [education]
    for i, education_school_data in enumerate(education_school_value):
            education[f'education_school_{i}'] = education_school_data
    for i, education_year_data in enumerate(education_year_value):
            education[f'education_year_{i}'] = education_year_data
    for i, education_course_data in enumerate(education_course_value):
            education[f'education_course_{i}'] = education_course_data
    
    # print(edu)

#working experience
    company_name_value=[]
    position_value=[]
    salary_range_value=[]
    profession_value = []
    company_name = my['company_name'][1:-1].split(", ")
    position = my['position'][1:-1].split(", ")
    salary_range = my['salary_range'][1:-1].split(", ")
    profession = my['profession'][1:-1].split(", ")
    for company_name_x in company_name:
        company_name_value.append(company_name_x[1:-1])
    for position_x in position:
        position_value.append(position_x[1:-1])
    for salary_range_x in salary_range:
        salary_range_value.append(salary_range_x[1:-1])
    for profession_x in profession:
        profession_value.append(profession_x[1:-1])
    working={}
    wor = [working]
    for i, company_name_data in enumerate(company_name_value):
            working[f'company_name_{i}'] = company_name_data
    for i, position_data in enumerate(position_value):
            working[f'position_{i}'] = position_data
    for i, salary_range_data in enumerate(salary_range_value):
            working[f'salary_range_{i}'] = salary_range_data
    for i, profession_data in enumerate(profession_value):
            working[f'profession_{i}'] = profession_data
    # print(wor)

#intrest
    
    
    your_intrest_value=[]
    your_intrest = my['your_intrest'][1:-1].split(", ")
    for i, your_intrest_data in enumerate(your_intrest):
            your_intrest_value.append({'intrest':your_intrest_data[1:-1]})
 
    inte=your_intrest_value
    # print(your_intrest_value)

    yourinterest = mydata[0]['your_intrest']
    x = yourinterest.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthyourinterest = x.split(",")
    # print(lengthyourinterest)

    interestlist = ["Music","Travel","Gaming","Reading","Photograph","Writing","Sports","Artist",
                    "Singing","Custom","Dancer","Speaking"]

#non intrest
    
    
    non_intrest_value=[]
    non_intrest = my['non_intrest'][1:-1].split(", ")
    for i, non_intrest_data in enumerate(non_intrest):
            non_intrest_value.append({'non_intrest':non_intrest_data[1:-1]})
 
    non_inte=non_intrest_value
    # print(non_inte)

    yournoninterest = mydata[0]['non_intrest']
    non = yournoninterest.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthyournoninterest = non.split(",")

#complexion
    complexion = mydata[0]['complexion']
    com = complexion.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthcomplexion= com.split(",")
    # print(lengthcomplexion)

    complexionlist = ["Dark","Medium","ModerateFaIr","FaIr","VeryFair"]

#food taste
    food_taste = mydata[0]['food_taste']
    ft = food_taste.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthfood_taste= ft.split(",")
    # print(lengthfood_taste)

    food_tastelist = ["Sweezt","Bitter","UmamI","Salt","Sour","Spicy"]

#gallery

    gall = mydata[0]['gallery']
    ga = gall.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthgallery= ga.split(",")

    if request.method == 'POST':
        if 'profile_tag' in request.POST:
            files={}
            data = {
            'profile_tag': request.POST['profile_tag'],
            }
            print(data)
        
        elif 'profile_picture' in request.FILES:
            data = {}
            files = {
            'profile_picture': request.FILES['profile_picture'],
            }
            print(files)

        elif 'about_candidate' in request.POST:
            files={}
            data = {
            'about_candidate': request.POST['about_candidate'],
            }
            print(data)
            
        elif 'current_status' in request.POST:
            files={}
            data = {
            'current_status': request.POST['current_status'],
            }
            print(data)
        elif 'address' in request.POST:
            files={}
            data = {
            'address': request.POST['address'],
            'primary_phone_number': request.POST['primary_phone_number'],
           'primary_email': request.POST['primary_email'],
            }
            print(data)
        elif 'contact_email' in request.POST:
            files={}
            data = {
            'contact_email': request.POST['contact_email'],
            'contact_phone': request.POST['contact_phone'],
            'whatsapp': request.POST['whatsapp'],
            }
            print(data)
        elif 'height' in request.POST:
            files={}
            data = {
            'height': request.POST['height'],
            'weight': request.POST['weight'],
            'age': request.POST['age'],
           'blood_group': request.POST['blood_group'],
           'marital_status': request.POST['marital_status'],
           'religion': request.POST['religion'],
           'primary_email': request.POST['primary_email'],
           'primary_phone_number': request.POST['primary_phone_number'],
           'education_school': request.POST['education_school'],
           'profession': request.POST['profession'],
           'orphan': request.POST['orphan'],
            }
            print(data)
        elif 'father_name' in request.POST:
            files={}
            data = {
            'father_name': request.POST['father_name'],
            'father_country': request.POST['father_country'],
            'father_job': request.POST['father_job'],
           'mother_name': request.POST['mother_name'],
           'mother_country': request.POST['mother_country'],
           'mother_job': request.POST['mother_job'],
           'father_family_name': request.POST['father_family_name'],
           'mother_family_name': request.POST['mother_family_name']
            }
            print(data)
        elif 'sibling_nameadd' in request.POST:
            files={}
            data = {
            'sibling_nameadd': request.POST['sibling_nameadd'],
            'sibling_relation': request.POST['sibling_relation'],
            'sibling_occupation': request.POST['sibling_occupation']
            }
            print(data)
        elif 'sibling_nameedit' in request.POST:
            files={}
            data = {
            'sibling_nameedit': request.POST.getlist('sibling_nameedit'),
            'sibling_relation': request.POST.getlist('sibling_relation'),
            'sibling_occupation': request.POST.getlist('sibling_occupation')
            }
            print(data)
        
        elif 'education_schooladd' in request.POST:
            files={}
            data = {
            'education_schooladd': request.POST['education_schooladd'],
            'education_year': request.POST['education_year'],
            'education_course': request.POST['education_course']
            }
            print(data)
        elif 'education_schooledit' in request.POST:
            files={}
            data = {
            'education_schooledit': request.POST.getlist('education_schooledit'),
            'education_year': request.POST.getlist('education_year'),
            'education_course': request.POST.getlist('education_course')
            }
            print(data)
        
        elif 'company_nameadd' in request.POST:
            files={}
            data = {
            'company_nameadd': request.POST['company_nameadd'],
            'position': request.POST['position'],
            'salary_range': request.POST['salary_range']
            }
            print(data)
        elif 'company_nameedit' in request.POST:
            files={}
            data = {
            'company_nameedit': request.POST.getlist('company_nameedit'),
            'position': request.POST.getlist('position'),
            'salary_range': request.POST.getlist('salary_range')
            }
            print(data)
        elif 'your_intrest' in request.POST:
            files={}
            data = {
            'your_intrest': request.POST.getlist('your_intrest')
            }
            print(data)
        
        elif 'non_intrest' in request.POST:
            files={}
            data = {
            'non_intrest': request.POST.getlist('non_intrest'),
            }
            print(data)
        
        elif 'complexion' in request.POST:
            files={}
            data = {
            'complexion': request.POST.getlist('complexion')
            }
            print(data)
        
        elif 'food_taste' in request.POST:
            files={}
            data = {
            'food_taste': request.POST.getlist('food_taste')
            }
            print(data)
        
        elif 'selfie' in request.FILES:
            data = {}
            files = {
            'selfie': request.FILES['selfie'],
            }
            print(files)

        elif 'full_size_image' in request.FILES:
            data = {}
            files = {
            'full_size_image': request.FILES['full_size_image'],
            }
            print(files)

        elif 'family' in request.FILES:
            data = {}
            files = {
            'family': request.FILES['family'],
            }
            print(files)

        elif 'gallery' in request.FILES:
            data = {}
            files = {}
            aa = request.FILES.getlist('gallery')
            for i, file_data in enumerate(aa):
                files[f'file_{i}'] = file_data
            print(files)
        elif 'gallerydelete' in request.POST:
            files={}
            data={
                'gallerydelete': request.POST['gallerydelete']
                }
            print(request.POST)
            
        else:
            files={}
            data={}
        # UHQLJ1L7CNH
        response = requests.post(f"http://127.0.0.1:3000/about_candidate/{id}",data = data,files = files)
        # LQS3Q7LMUG1
        # print(response)
        print(response.status_code)
        # print(response.text)
        return redirect(f"/profile_page/{id}")
        # uidd = (response.text[1:-1])
        # print(uidd)

#     return render(request,'profile_page.html',{'profile_pic':profile_pic,'mydata':mydata,
#                                                'lengthyourinterest':lengthyourinterest,
#                                                'interestlist':interestlist,
#                                                'lengthyournoninterest':lengthyournoninterest,
#                                                'lengthcomplexion':lengthcomplexion,
#                                                'complexionlist':complexionlist,
#                                                'lengthfood_taste':lengthfood_taste,
#                                                'food_tastelist':food_tastelist,
#                                                'lengthgallery':lengthgallery})
    context={
      'profile_pic':profile_pic,
      'mydata':mydata,
      'sibling':sib,
      'education':edu,
      'working':wor,
      'intrest':inte,
      'interestlist':interestlist,
      'lengthyourinterest':lengthyourinterest,
      'non_intrest':non_inte,
      'lengthyournoninterest':lengthyournoninterest,
      'complexionlist':complexionlist,
      'lengthcomplexion':lengthcomplexion,
      'lengthfood_taste':lengthfood_taste,
      'food_tastelist':food_tastelist,
        'lengthgallery':lengthgallery,
             }
    return render(request,'profile_page.html',context)

# High light profile
def profilehiglight(request):
    coun = countries.objects.all()
    if request.method == "POST":
        profile_finder_email = request.session['email']
        form = Highlight_Profile(request.POST)
        if form.is_valid():
            country_multiple = request.POST.getlist('country_multiple[]')
            state_multiple = request.POST['state_multiple']
            district_multiple = request.POST['district_multiple']
            languages_multiple = request.POST.getlist('languages_multiple[]')
            age_group = request.POST['age_group']
            total_Number_of_Views = request.POST['total_Number_of_Views']
            how_many_days_required = request.POST['how_many_days_required']
            how_many_times_Repeat_per_day = request.POST['how_many_times_Repeat_per_day']

            profile_finder.objects.filter(email=profile_finder_email).update(country_multiple=country_multiple,state_multiple=state_multiple,district_multiple=district_multiple,languages_multiple=languages_multiple,age_group=age_group,total_Number_of_Views=total_Number_of_Views,how_many_days_required=how_many_days_required,how_many_times_Repeat_per_day=how_many_times_Repeat_per_day)
    
    return render(request,'profilehiglight.html',{'countries':coun})

def highlight_profile(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata = [my]
    if request.method=="POST":
        return redirect(f"/highlight_payment/{id}")
    context ={
        'mydata':mydata
    }
    return render(request,'highlight_profile.html',context)

def highlight_payment(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata = [my]
    if request.method=="POST":
        return redirect(f"/profile_page/{id}")
    context ={
        'mydata':mydata
    }
    return render(request,'highlight_payment.html',context)


#payment page
def payment(request):
    return render(request,'payment.html')

#matching list
def matching_list(request,id):
    # profile_finder_email = request.session['email']
    # mydata = profile_finder.objects.filter(email=profile_finder_email).values() 
    #mydatalen = len(mydata)
   
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    my_intrest = my['your_intrest'][1:-2].replace("'","").replace(" ","").split(",")
    non_intrest = my['non_intrest'][1:-2].replace("'","").replace(" ","").split(",")
    complexion = my['complexion'][1:-2].replace("'","").replace(" ","").split(",")
    food_taste = my['food_taste'][1:-2].replace("'","").replace(" ","").split(",")
    daily_diet_plan = my['daily_diet_plan'][1:-2].replace("'","").replace(" ","").split(",")
    
    #find gender
    if [my][0]['gender'] == "female":
       male = requests.get(f"http://127.0.0.1:3000/all_male_user_data/{id}").json()
       alldata = male[id]
       
    elif [my][0]['gender'] == "male":
        female = requests.get(f"http://127.0.0.1:3000/all_female_user_data/{id}").json()
        alldata = female[id]
        # print(alldata)
    global neww
    neww = []
    your_intrest_value=x=[]
    for x in alldata:
        #sibling details
        # print(x['sibling_name'])
        sibling_name_value=[]
        sibling_relation_value=[]
        sibling_occupation_value=[]
        sibling_name = x['sibling_name'][1:-1].split(", ")
        sibling_relation = x['sibling_relation'][1:-1].split(", ")
        sibling_occupation = x['sibling_occupation'][1:-1].split(", ")
        for sibling_name_x in sibling_name:
            sibling_name_value.append(sibling_name_x[1:-1])
        for sibling_relation_x in sibling_relation:
            sibling_relation_value.append(sibling_relation_x[1:-1])
        for sibling_occupation_x in sibling_occupation:
            sibling_occupation_value.append(sibling_occupation_x[1:-1])
        # print(type(sibling_name_value))
        sibling=x
        # sib = [sibling]
        for i, sibling_name_data in enumerate(sibling_name_value):
                sibling[f'sibling_name_{i}'] = sibling_name_data
        for i, sibling_relation_data in enumerate(sibling_relation_value):
                sibling[f'sibling_relation_{i}'] = sibling_relation_data
        for i, sibling_occupation_data in enumerate(sibling_occupation_value):
                sibling[f'sibling_occupation_{i}'] = sibling_occupation_data
        
        neww.append(sibling)
        #education
        education_school_value=[]
        education_year_value=[]
        education_course_value=[]
        education_school = x['education_school'][1:-1].split(", ")
        education_year = x['education_year'][1:-1].split(", ")
        education_course = x['education_course'][1:-1].split(", ")
        for education_school_x in education_school:
            education_school_value.append(education_school_x[1:-1])
        for education_year_x in education_year:
            education_year_value.append(education_year_x[1:-1])
        for education_course_x in education_course:
            education_course_value.append(education_course_x[1:-1])
        education=x
        # edu = [education]
        for i, education_school_data in enumerate(education_school_value):
                education[f'education_school_{i}'] = education_school_data
        for i, education_year_data in enumerate(education_year_value):
                education[f'education_year_{i}'] = education_year_data
        for i, education_course_data in enumerate(education_course_value):
                education[f'education_course_{i}'] = education_course_data
        neww.append(education)
        #working experience
        company_name_value=[]
        position_value=[]
        salary_range_value=[]
        profession_value = []
        company_name = x['company_name'][1:-1].split(", ")
        position = x['position'][1:-1].split(", ")
        salary_range = x['salary_range'][1:-1].split(", ")
        profession = x['profession'][1:-1].split(", ")
        for company_name_x in company_name:
            company_name_value.append(company_name_x[1:-1])
        for position_x in position:
            position_value.append(position_x[1:-1])
        for salary_range_x in salary_range:
            salary_range_value.append(salary_range_x[1:-1])
        for profession_x in profession:
            profession_value.append(profession_x[1:-1])
        working=x
        # wor = [working]
        for i, company_name_data in enumerate(company_name_value):
                working[f'company_name_{i}'] = company_name_data
        for i, position_data in enumerate(position_value):
                working[f'position_{i}'] = position_data
        for i, salary_range_data in enumerate(salary_range_value):
                working[f'salary_range_{i}'] = salary_range_data
        for i, profession_data in enumerate(profession_value):
                working[f'profession_{i}'] = profession_data
        neww.append(working)
        # print(wor)
        #intrest
        intrestt = x
        your_intrest = x['your_intrest'][1:-1].replace("'","").replace(" ","").split(",")
        # print(your_intrest)
        for i, your_intrest_data in enumerate(your_intrest):
                # neww.append({'myintrest':your_intrest_data[1:-1]})
                intrestt[f'intrest_{i}'] = your_intrest_data
        # print(intrestt)
        neww.append(intrestt)
        #non-intrest
        non_intrestt = x
        n_intrest = x['non_intrest'][1:-1].replace("'","").replace(" ","").split(",")
        # print(your_intrest)
        for i, your_intrest_data in enumerate(n_intrest):
                # neww.append({'myintrest':your_intrest_data[1:-1]})
                non_intrestt[f'non_intrest_{i}'] = your_intrest_data
        neww.append(non_intrestt)
        #complexion
        complexion_list = x
        complexion_change_list = x['complexion'][1:-1].replace("'","").replace(" ","").split(",")
        # print(your_intrest)
        for i, your_intrest_data in enumerate(complexion_change_list):
                # neww.append({'myintrest':your_intrest_data[1:-1]})
                complexion_list[f'complexion_{i}'] = your_intrest_data
        neww.append(complexion_list)
        #food_taste
        food_taste_list = x
        food_taste_change_list = x['food_taste'][1:-1].replace("'","").replace(" ","").split(",")
        # print(your_intrest)
        for i, your_intrest_data in enumerate(food_taste_change_list):
                # neww.append({'myintrest':your_intrest_data[1:-1]})
                food_taste_list[f'food_taste_{i}'] = your_intrest_data
        neww.append(food_taste_list)
    

    
    # percentage
    alluserdata =[]
    for x in alldata:
        comparision_intrest = x['your_intrest'][1:-2].replace("'","").replace(" ","").split(",")
        comparision_non_intrest = x['non_intrest'][1:-2].replace("'","").replace(" ","").split(",")
        comparision_complexion = x['complexion'][1:-2].replace("'","").replace(" ","").split(",")
        comparision_food_taste = x['food_taste'][1:-2].replace("'","").replace(" ","").split(",")
        comparision_daily_diet_plan = x['daily_diet_plan'][1:-2].replace("'","").replace(" ","").split(",")
        #intrest
        ci=0
        for i,y in enumerate(my_intrest):
          if y in comparision_intrest:
            ci+=len(y[1:-2].replace("'","").replace(" ","").split(","))
        # print("")
        inte= int((ci*100)/len(my_intrest))
        #non_intrest
        cn = 0
        for j,z in enumerate(non_intrest):
          if z in comparision_non_intrest:
            cn+=len(z[1:-2].replace("'","").replace(" ","").split(","))
        # print("")
        ninte = int((cn*100)/len(non_intrest))
        #complexion
        co = 0
        for j,h in enumerate(complexion):
          if h in comparision_complexion:
            co+=len(h[1:-2].replace("'","").replace(" ","").split(","))
        # print("")
        comp = int((co*100)/len(complexion))
        #food_taste
        ft = 0
        for j,f in enumerate(food_taste):
          if f in comparision_food_taste:
            ft+=len(f[1:-2].replace("'","").replace(" ","").split(","))
        # print("")
        food = int((ft*100)/len(food_taste))
        #daily dite plan
        ddp = 0
        for j,dp in enumerate(daily_diet_plan):
          if dp in comparision_daily_diet_plan:
            ddp+=len(dp[1:-2].replace("'","").replace(" ","").split(","))
        # print("")
        diet = int((ddp*100)/len(daily_diet_plan))
        total = inte+ninte+comp+food+diet
        x['percentage'] = int(total/5)
        alluserdata.append(x)
    lenofid=[]
    for le in alluserdata:
        if le['percentage'] > 50:
            lenofid.append(le)
    print(len(lenofid))
    print(lenofid)
        
    profile_pic = [my][0]['profile_picture']
    #for target
    for x in alldata:
        res = ''.join([j for j in x['uid'] if not j.isdigit()])
        x['target']=res
        alluserdata.append(x)
    # print(alluserdata)
    
    #my favorite list
    sent = requests.get(f"http://127.0.0.1:3000/favorites/{id}").json()
    # print(sent)
    favoritemy=[]
    for f in sent[id]:
       favoritemy.append(f['uid'])

    mydata = [my]
    my_preference="1"
    
    #request sent
    if request.method == "POST":
        if 'request_phone_number' in request.POST:
            print(request.POST)
            data = {'received_uid':request.POST['received_uid']}
            for x in request.POST:
                if len(request.POST.getlist(x)) == 2:
                    data[x] = request.POST.getlist(x)[0]
                elif request.POST[x] == "":
                    data[x] = "none"
            print(data)
            # response = requests.post('http://54.159.186.219:8000/requested_list/',data=data)
            response = requests.post(f'http://127.0.0.1:3000/requested_list/{id}',data=data)
        
        elif 'reason' in request.POST:
            print(request.POST)
            # response = requests.post('http://54.159.186.219:8000/block/',data=data)
            response = requests.post(f'http://127.0.0.1:3000/block/{id}',data=request.POST)
        
        elif 'myfavorite_id' in request.POST:
            print(request.POST)
            response = requests.post(f'http://127.0.0.1:3000/favorites/{id}',data=request.POST)
            return redirect(f"/matching_list/{id}")

        elif 'marital_status' in request.POST:
            print(request.POST)
            matc={
                'a':request.POST['marital_status'],
                'b':request.POST['physical_mental_status'],
                'c':request.POST['email'],
                'd':request.POST['family_status'],
                'e':request.POST['age'],
                'f':request.POST['height'],
                'g':request.POST['education'],
                'h':request.POST['Working']
            }
            
            p = []
            for x in alldata:
                if matc['a'] == x['marital_status'] :
                    a = x['uid']
                elif matc['a'] == "":
                    a = ""
                else:
                    a = "no"
                if matc['b'] == x['physical_mental_status']:
                    b = x['uid']
                elif matc['b'] == "":
                    b = ""
                else:
                    b = "no"
                if matc['c'] == x['email'] :
                    c = x['uid']
                elif matc['c'] == "":
                    c = ""
                else:
                    c = "no"
                if matc['d'] == x['family_status']:
                    d = x['uid']
                elif matc['d'] == "":
                    d = ""
                else:
                    d = "no"
                if matc['e'] == x['age']:
                    e = x['uid']
                elif matc['e'] == "":
                    e = ""
                else:
                    e = "no"
                if matc['f'] == x['height']:
                    f = x['uid']
                elif matc['f'] == "":
                    f = ""
                else:
                    f = "no"
                if matc['g'] == x['education_major']:
                    g = x['uid']
                elif matc['g'] == "":
                    g = ""
                else:
                    g = "no"
                if matc['h'] in x['are_you_working_now']:
                    h = x['uid']
                elif matc['h'] == "":
                    h = ""
                else:
                    h = "no"
                pref = {a,b,c,d,e,f,g,h}
                print(pref)
                if "no" not in pref:
                    pref.remove("")
                    for con in pref:
                       p.append(con)
                       print(p)
                # else:
                #     pref.remove("")
                #     print(pref)

            # print(p)
                    
            my_preference=[]
            userlist=[]
            for y in alluserdata:
                userlist.append(y['uid'])
            # print(userlist)
            for x in p:
                # print(x)
                numb = userlist.index(x)
                # print(numb)
                get_Selected = alluserdata[numb]
                my_preference.append(get_Selected)
            print(my_preference)
            
    # print(alldata[::-1])                           
    context = {'mydata':mydata,
               'alldata':alldata[::-1],
               'neww':neww,
               'profile_pic':profile_pic,
               'my_preference':my_preference,
               'your_intrest_value':your_intrest_value,
               'lenofid':lenofid,
               'sent':sent[id],
               'favoritemy':favoritemy,
               }
    # print(context)
    return render(request,'matching_list.html',context)
def match_list_person(request):
    # alluserdata_one =[]
    # alldata = requests.get("http://127.0.0.1:3000/alluserdata/").json()
    # my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    # for x in alldata:
    #     res = ''.join([j for j in x['uid'] if not j.isdigit()])
    #     print(res)
    #     x['target']=res
    #     alluserdata_one.append(x)
    # print(alluserdata_one)
    context = {'alldata_one':"alluserdata_one",
           }
    return render(request,"match_list_person.html",context)
def viewallmatch(request,id):
    alluserdata_two =[]
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata=[my]
    #find gender
    if [my][0]['gender'] == "female":
       male = requests.get(f"http://127.0.0.1:3000/all_male_user_data/{id}").json()
       alldata = male[id]
       
    elif [my][0]['gender'] == "male":
        female = requests.get(f"http://127.0.0.1:3000/all_female_user_data/{id}").json()
        alldata = female[id]
        # print(alldata)
    for x in alldata:
        res = ''.join([j for j in x['uid'] if not j.isdigit()])
        print(res)
        x['target']=res
        alluserdata_two.append(x)
    print(alluserdata_two)
    matching_list(request,id)
    context = {'alldata':alluserdata_two,
               'mydata':mydata,
               'profile_pic':profile_pic,
               'neww':neww,
           }
    return render(request,"viewallmatch.html",context)

    
def menu_header(request):
    # my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    # mydata = [my]
    # context={'keyy':my}
    # print(mydata)
    return render(request,'menu_header.html')

def package_matching(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    # print(sent[id])
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'package_matching.html',context)

def requested_list(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    sent = requests.get(f"http://127.0.0.1:3000/requested_list/{id}").json()
    print(sent)
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'sent':sent[id],
               }
    return render(request,'requested_list.html',context)
def received(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    received = requests.get(f"http://127.0.0.1:3000/received_list/{id}").json()
    mydata=[my]
    rece = received[id]
    # print(rece)

    if request.method == "POST":
        print(request.POST)
        received = requests.post(f"http://127.0.0.1:3000/received_list/{id}",data = request.POST)
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'received':rece,
               }
    return render(request,'received.html',context)
#favoites
def myfavorites(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    sent = requests.get(f"http://127.0.0.1:3000/favorites/{id}").json()
    # print(sent[id])
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'sent':sent[id],
               }
    return render(request,'myfavorites.html',context)

def favorites_to_me(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    sent = requests.get(f"http://127.0.0.1:3000/favorites_to_me/{id}").json()
    # print(sent[id])
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'sent':sent[id],
               }
    return render(request,'favorites_to_me.html',context)

def saved_search(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    my_sav = requests.get(f"http://127.0.0.1:3000/saved_search/{id}").json()
    # print(my_sav)
    if request.method=="POST":
        
        if 'tag' in request.POST:
            print(request.POST)
            mat={
                    'tag':request.POST['tag'],
                    'country':request.POST['country'],
                    'city':request.POST['city'],
                    'age':request.POST['age'],
                    'complexion':request.POST.getlist('complexion'),
                    'gender':request.POST['gender'],
                    'denomination':request.POST['denomination'] 
                  
                }
        elif 'tag_edit' in request.POST: 
            print(request.POST)
            mat={
                    'tag_edit':request.POST['tag_edit'],
                    'country':request.POST['country'],
                    'city':request.POST['city'],
                    'age':request.POST['age'],
                    'complexion':request.POST.getlist('complexion'),
                    'gender':request.POST['gender'],
                    'denomination':request.POST['denomination'],
                    'id':request.POST['id']
                  
                }
        elif 'remove' in request.POST: 
            print(request.POST)
            mat={'remove':request.POST['remove']}
            
        received = requests.post(f"http://127.0.0.1:3000/saved_search/{id}",data = mat)

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'my_sav':my_sav[id],
               }
    return render(request,'saved_search.html',context)

def saved_search_view_profile(request,uid,id):
    print(id)
    my = requests.get(f"http://127.0.0.1:3000/alldata/{uid}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    my_sav = requests.get(f"http://127.0.0.1:3000/saved_search/{uid}").json()
    separated_list=[]
    print(my_sav)
    for x in my_sav[uid]:
        print(len(x['filterd_data']))
        if len(x['filterd_data']) != 2:
            if x['id'] == int(id):
                filter = x['filterd_data'][1:-2].replace("'","").replace(" ","").split(",")
                for y in filter:
                    all_filter_data = requests.get(f"http://127.0.0.1:3000/alldata/{y}").json()
                    print(all_filter_data)
                    separated_list.append(all_filter_data)
            else:
                print("no")
        else:
            separated_list.append("NO MATCHING LIST")
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'my_sav':separated_list,
               }
    return render(request,'saved_search_view_profile.html',context)


def follow_request1(request):
    profile_finder_email=request.session['email']
    id = profile_finder.objects.filter(email=profile_finder_email).values()
    idvalue = id[0]['id']
    profile_pic = id[0]['profile_picture']
    datas = follow_request.objects.filter(receiver_id=idvalue).values()
    receiverprofileimage = []
    for x in range(len(datas)):
        sender_id = datas[x]['sender_id']
        receiver_details = profile_finder.objects.filter(id=sender_id).values()
        profil_image = receiver_details[0]['profile_picture']
        receiverprofileimage.append(profil_image)
        print(receiverprofileimage)
        #print(sender[x]['profile_picture'])
    receiverprofileimageli = zip(datas,receiverprofileimage) 



    sender = follow_request.objects.filter(sender_id=idvalue).values()
    sentprofileimage = []
    for x in range(len(sender)):
        receive_id = sender[x]['receiver_id']
        receiver_details = profile_finder.objects.filter(id=receive_id).values()
        profil_image = receiver_details[0]['profile_picture']
        sentprofileimage.append(profil_image)
        print(sentprofileimage)
        #print(sender[x]['profile_picture'])
    sentprofileimageli = zip(sender,sentprofileimage)   

    if 'buttaccept' in request.POST:
        sender_id = request.POST['sender_id']
        receiver_id = request.POST['receiver_id']
        accept = request.POST['accept']
        
        follow_request.objects.filter(sender_id=sender_id).filter(receiver_id=receiver_id).update(
            accept=accept
        )
        #cursor = connections['default'].cursor()
        #cursor.execute("INSERT INTO chat_thread(field1,field2) VALUES( %s , %s )", [value1, value2])
        Thread.objects.create(first_person=sender_id,second_person=receiver_id)
        #Thread.objects.raw("INSERT INTO `chat_thread`(`first_person_id`, `second_person_id`) VALUES (sender_id,receiver_id)")
        print("Thred Created Successfully")



    elif 'buttreject' in request.POST:
        sender_id = request.POST['sender_id']
        receiver_id = request.POST['receiver_id']
        accept = request.POST['accept']
        
        follow_request.objects.filter(sender_id=sender_id).filter(receiver_id=receiver_id).update(
            accept=accept
        )
        
    return render(request,'request_received.html',{'datas':datas,'sender':sender,
                                                   'sentprofileimage':sentprofileimageli,
                                                   'receiverprofileimageli':receiverprofileimageli,
                                                   'idvalue':idvalue,"profile_pic":profile_pic})

def follow_requestsent(request,id):
    # profile_finder_email=request.session['email']
   
    # id = profile_finder.objects.filter(email=profile_finder_email).values()
    # idvalue = id[0]['id']
    # print(idvalue)
    if request.method == "POST":
        form = follow_requestForm(request.POST)
        if form.is_valid():
            sender_id = request.POST['sender_id']
            #print("Sender :"+sender_id) 
            receiver_id = request.POST['receiver_id']
            #print("Receive :"+receiver_id)
            already_sent = follow_request.objects.filter(sender_id=sender_id).filter(receiver_id=receiver_id).values()
            already_sent_len = len(already_sent)
            #print(already_sent_len)
            if(already_sent_len == 0):
                form.save()
                return JsonResponse("Request Sent Successfully", safe=False)
            else:
                return JsonResponse("Request Already Sent", safe=False)
        else:
            return JsonResponse("Failure", safe=False)
    #return render(request,'request_sent.html',{'idvalue':idvalue})
    return render(request,'request_sent.html')

def test2(request):
    # import random
    # import string
    # allowed_chars = ''.join((string.ascii_letters, string.digits))
    # unique_id = ''.join(random.choice(allowed_chars) for _ in range(6))
    return HttpResponse("unique_id")




def happy_couples(request):
    return render(request,"sucess_story.html")

def happy_couples_test(request):
    return render(request,"sucess_story copy.html")




#happy couple 


def happycouple(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata = [my]
    happy_couples_all_data = requests.get("http://127.0.0.1:3000/happy_couples_all/").json()
    # print(happy_couples_all_data)
    all_happy_couple=[]
    for x in happy_couples_all_data:
        allimage = x['image_videous'][1:-2].replace("'","").replace(" ","").split(",")
        x['file1'] =allimage[0]
        all_happy_couple.append(x)
    
    
    if request.method=="POST":
        if "groom_id" in request.POST:
           print(request.POST)
           global groom_id
           groom_id = request.POST['groom_id']  
        #    print(groom_id)    
           return redirect(f"/success_story/{id}")
        #    uid = request.POST['groom_id']
        #    requests.post(f"http://127.0.0.1:3000/happy_couples_one/{uid}",data = request.POST)
        
       

        # return redirect(f"/package_amount/{id}")
    # a = upload.objects.all().values()
    # for x in a:
    #     z=dict(x)
    #     q=z.values()
    #     for y in q:
    #       new.append(y)
    # t = (set(new))
    # print(list(t))
     #get signin user email
    # profile_finder_email = request.session['email']
    #get user details
    # main = (profile_finder.objects.filter(email=profile_finder_email).values())
    # mainn = (profile_finder.objects.filter(email=profile_finder_email).all())
    # #get a user name
    # for x in main:
    #     ee=x["name"]
    # a = upload.objects.filter(useremail=profile_finder_email)
    # for y in a:
    #     new.append(y)
    # sel=[new[0]]
    # context = {
    #     'key':sel
    # }
    # return render(request,'happy_couples.html',context)
    
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'happy_couples_all_data':all_happy_couple,
               }
    return render(request,'happycouples.html',context)

def success_Story(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata = [my]
    print("success")
    happycouple(request,id)
    print(groom_id)
    uidd = groom_id

    onedata = requests.get("http://127.0.0.1:3000/happy_couples_all/").json()
    all_happy_couple=[]
    allimg={}
    for x in onedata:
        if uidd == x['groom_id']:
           allimage = x['image_videous'][1:-2].replace("'","").replace(" ","").split(",")
           x['file1'] =allimage[0]
           allimg['allimage'] =allimage[1:]
           all_happy_couple.append(x)
    print(all_happy_couple)
    print(allimage)
        # return redirect(f"/package_amount/{id}")
    context ={
        'mydata':mydata,
        'onedata':onedata,
        'uidd':uidd,
        'allimage':allimage[1:]
    }
    return render(request,'success_story.html',context)

def package(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata = [my]
    # if request.method=="POST":
    #     print(request.POST)
    #     return redirect(f"/package_amount/{id}")
    context ={
        'mydata':mydata
    }
    return render(request,'package.html',context)

def package_amount(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata = [my]
    if request.method=="POST":
        return redirect(f"/happy_couples_upload/{id}")
    context ={
        'mydata':mydata,
        'profile_pic':profile_pic,
    }
    return render(request,'package_amount.html',context)

def happy_couples_upload(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata = [my]
    if request.method == "POST":
        # print(request.POST)
        images = request.FILES.getlist('image_videous')
        files = {}
        for i, file_data in enumerate(images):
            files[f'file_{i}'] = file_data
        data = {
            'groom_name':request.POST['groom_name'],
            'groom_id':request.POST['groom_id'],
            'bride_name':request.POST['bride_name'],
            'bride_id':request.POST['bride_id'],
            'date_of_marriage':request.POST['date_of_marriage'],
            'worde_about_marriyo':request.POST['worde_about_marriyo'],
            
        }
        print(data)
        print(files)
        happy = requests.post(f"http://127.0.0.1:3000/happy_couples/{id}",data = data,files=files)

        
    context ={
        'mydata':mydata,
        'profile_pic':profile_pic,
    }
    return render(request,'happy_couples_upload.html',context)


# def uploadyours(request):
#     #get signin user email
#     profile_finder_email = request.session['email']
#     print(profile_finder_email)
#     #get user details
#     main = (profile_finder.objects.filter(email=profile_finder_email).all())
#     a = upload.objects.filter(useremail=profile_finder_email)
#     # for i in 
#     # for x in main:
#     #     print(x)
#     #     ee=x["name"]
#     name = serializers.serialize("json",main)
#     context={'name':name}
#     if "a" in "0":
#         a.delete()
#         return HttpResponse("deleted")
#     else:
#      if request.method=='POST':
#         fullname = request.POST['fullname']
#         date_of_marriage = request.POST['date_of_marriage']
#         words_about_marrio = request.POST['words_about_marrio']
#         marriage_photos = request.FILES.getlist('marriage_photos')

#         for image in marriage_photos:
#             form = upload.objects.create(
#                 useremail = profile_finder_email,
#                 fullname=fullname,
#                 date_of_marriage=date_of_marriage,
#                 words_about_marrio=words_about_marrio,
#                 marriage_photos=image,
#               )
#             form.save()
#             return redirect('/sucess_story')

#     return render(request,'uploadyours.html',context)

def happy_couples(request):
    new=[]
    #get signin user email
    profile_finder_email = request.session['email']
    #get user details
    main = (profile_finder.objects.filter(email=profile_finder_email).values())
    mainn = (profile_finder.objects.filter(email=profile_finder_email).all())
    #get a user name
    for x in main:
        ee=x["name"]
    a = upload.objects.filter(useremail=profile_finder_email)
    for y in a:
        new.append(y)
    sel=[new[0]]
    print(type(sel))
    b =  upload.objects.filter(useremail=profile_finder_email)
    selee = b[0:3]
    print((selee))
    #convert json 
    name = serializers.serialize("json",mainn)
    context = {
        'key': sel,
        'image':selee,
        'main':main,
        'name':name,
    }
    return render(request, 'sucess_story.html', context)

# def block(request):
#     print('enter the function')
#     if request.method=='POST':
        
#         profile_finder_email = request.session['email']
#         form = Block(request.POST)
#         if form.is_valid():
#             block_list = request.POST['block_list']
#             data = profile_finder.objects.filter(email=profile_finder_email).values()
#             gen = data[0]['block_list']
#             block=[]
#             if gen == None:
#                 block.append(block_list)
#             else:
#                 block.append(gen)
#                 block.append(block_list)
            
            
            
#             print(block)
#             profile_finder.objects.filter(email=profile_finder_email).update(block_list= block)
#     return redirect('/matching_list') 
    

def block(request):
    print('enter the function')
    if request.method == 'POST':
        profile_finder_email = request.session['email']
        form = Block(request.POST)
        if form.is_valid():
            block_list = request.POST['block_list']
            data = profile_finder.objects.filter(email=profile_finder_email).values()
            gen = data[0]['block_list']
            block = []
            if gen:
                block = eval(gen)  # Convert the string representation to a list
            block.append(block_list)

            print(block)
            profile_finder.objects.filter(email=profile_finder_email).update(block_list=block)
    return redirect('/matching_list')
#settings
def settings_notification(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'settings_notification.html',context)

def settings_privacy(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'settings_privacy.html',context)

def settings_security(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'settings_security.html',context)

def settings_subscription(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'settings_subscription.html',context)

def settings_wallet(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'settings_wallet.html',context)

def settings_about(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'settings_about.html',context)

def wallet_add(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'wallet_add.html',context)

def muted_acc(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
               }
    return render(request,'muted_acc.html',context)

def blocked_acc(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    gender = [my][0]['gender']
    mydata=[my]
    my_block = requests.get(f"http://127.0.0.1:3000/block/{id}").json()
    # print(my_block)
    if request.method=="POST":
        print(request.POST)
        requests.post(f"http://127.0.0.1:3000/block/{id}",data=request.POST)
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'my_block':my_block[id],
               }
    return render(request,'blocked_acc.html',context)

def all_investigator(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()

    all_investigator = requests.get(f"http://127.0.0.1:3000/all_private_investigator_data").json()
    if request.method=="POST":
        print(request.POST)
        if "hire" in request.POST:
           print(request.POST)
           global hire_id
           hire_id = request.POST['hire']  
           return redirect(f"/hire_investigator/{id}")
    profile_pic = [my][0]['profile_picture']
    mydata=[my]
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'all_investigator':all_investigator,
           
               }

    return render(request,'all_investigator.html',context)

def hire_investigator(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata=[my]
    #redirect specific user
    all_investigator(request,id)
    print(hire_id)
    #all investigator data
    all_investigator_values = requests.get(f"http://127.0.0.1:3000/all_private_investigator_data").json()
    for  x in all_investigator_values:
        if x['uid'] == hire_id:
            specific_user = x
            print(specific_user)
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'specific_user':[specific_user],
               }

    return render(request,'hire_investigator.html',context)

def my_investigator(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    my_investigators = requests.get(f"http://127.0.0.1:3000/my_investigator/{id}").json()[id]
    profile_pic = [my][0]['profile_picture']
    mydata=[my]
    if "my_investigator" in request.POST:
           print(request.POST)
           global hire_id
           hire_id = request.POST['my_investigator']  
           return redirect(f"/my_investigator_question/{id}")
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
           'my_investigators':my_investigators,
               }

    return render(request,'my_investigator.html',context)

def my_investigator_question(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata=[my]
    my_investigator(request,id)
    print(hire_id)
    all_investigator_values = requests.get(f"http://127.0.0.1:3000/all_private_investigator_data").json()
    for  x in all_investigator_values:
        if x['uid'] == hire_id:
            specific_user = x
            print(specific_user)

    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
            'specific_user':[specific_user],
               }

    return render(request,'my_investigator_question.html',context)

def pi_payment(request,id):
    my = requests.get(f"http://127.0.0.1:3000/alldata/{id}").json()
    profile_pic = [my][0]['profile_picture']
    mydata=[my]
    context = {
            'mydata':mydata,
            'profile_pic':profile_pic,
           
               }

    return render(request,'pi_payment.html',context)