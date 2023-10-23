from django.db import models
# # from phonenumber_field.modelfields import PhoneNumberField
# # from phone_field import PhoneField

# # Create your models here.


# class profile_finder(models.Model):
#     email = models.TextField()
#     mobile = models.IntegerField()
#     password = models.TextField()
#     confirm_password = models.TextField()
#     referral_code = models.CharField(default=None, blank=True, null=True,max_length=6)
#     code = models.CharField(default=None, blank=True, null=True,max_length=6)
#     user_otp = models.CharField(default=None, blank=True, null=True,max_length=6)
#     idcard = models.FileField(upload_to = 'pictures',default=None, blank=True, null=True,max_length=500)
    
#     height = models.IntegerField(default=None, blank=True, null=True)
#     weight = models.IntegerField(default=None, blank=True, null=True)
#     martial = models.TextField(default=None, blank=True, null=True,max_length=500)
#     physical = models.TextField(default=None, blank=True, null=True,max_length=500)
#     birth_place = models.TextField(default=None, blank=True, null=True,max_length=500)
#     birth_country = models.TextField(default=None, blank=True, null=True,max_length=500)
#     birth_time = models.TextField(default=None, blank=True, null=True,max_length=500)
#     birth_city = models.TextField(default=None, blank=True, null=True,max_length=500)
#     orgin = models.TextField(default=None, blank=True, null=True,max_length=500)
#     r_country = models.TextField(default=None, blank=True, null=True,max_length=500)
#     r_state =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     denomination =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     blood_group =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     r_status = models.TextField(default=None, blank=True, null=True,max_length=500)
#     temple_name = models.TextField(default=None, blank=True, null=True,max_length=500)
#     street = models.TextField(default=None, blank=True, null=True,max_length=500)
#     post_code =  models.IntegerField(default=None, blank=True, null=True)
#     country = models.TextField(default=None, blank=True, null=True,max_length=500)
#     city = models.TextField(default=None, blank=True, null=True,max_length=500)
#     address_phone = models.IntegerField(default=None, blank=True, null=True)
#     diocese = models.TextField(default=None, blank=True, null=True,max_length=500)
#     local_admin = models.TextField(default=None, blank=True, null=True,max_length=500)
#     emergency_name = models.TextField(default=None, blank=True, null=True,max_length=500)
#     relation = models.TextField(default=None, blank=True, null=True,max_length=500)
#     emergency_number =  models.IntegerField(default=None, blank=True, null=True)
#     emergency_email = models.TextField(default=None, blank=True, null=True,max_length=500)
#     emergency_martial = models.TextField(default=None, blank=True, null=True,max_length=500)
#     emergency_occupation = models.TextField(default=None, blank=True, null=True,max_length=500)

#     emergency_name1 = models.TextField(default=None, blank=True, null=True,max_length=500)
#     relation1 = models.TextField(default=None, blank=True, null=True,max_length=500)
#     emergency_number1 =  models.IntegerField(default=None, blank=True, null=True)
#     emergency_email1 = models.TextField(default=None, blank=True, null=True,max_length=500)
#     emergency_martial1 = models.TextField(default=None, blank=True, null=True,max_length=500)
#     emergency_occupation1 = models.TextField(default=None, blank=True, null=True,max_length=500)
#     upload_idcard = models.FileField(upload_to = 'profileid',default=None, blank=True, null=True,max_length=500)
#     profile_picture = models.FileField(upload_to = 'profilepicture',default=None, blank=True, null=True,max_length=500)
#     dob = models.TextField(default=None, blank=True, null=True)

#     #Family Details Fields
#     family_status = models.TextField(default=None, blank=True, null=True)
#     family_fathername = models.TextField(default=None, blank=True, null=True)
#     family_fatherbirthcountry = models.TextField(default=None, blank=True, null=True)
#     family_fatherbirthcity = models.TextField(default=None , blank=True, null=True)
#     family_fatherjob = models.TextField(default=None, blank=True, null=True)
#     family_mothername         = models.TextField(default=None, blank=True, null=True)
#     family_motherbirthcountry = models.TextField(default=None, blank=True,null=True)
#     family_motherbirthcity    = models.TextField(default=None, blank=True,null=True)
#     family_motherjob          = models.TextField(default=None, blank=True,null=True)
#     family_sib1name = models.TextField(default=None,blank=True,null=True)
#     family_sib1relation = models.TextField(default=None,blank=True,null=True)
#     family_sib1young = models.TextField(default=None,blank=True,null=True)
#     family_sib1occupations = models.TextField(default=None,blank=True,null=True)
#     family_sib1martial = models.TextField(default=None,blank=True,null=True)
#     family_sib1email = models.TextField(default=None,blank=True,null=True)
#     family_sib1dob = models.TextField(default=None,blank=True,null=True)
#     #sib2
#     family_sib2name = models.TextField(default=None,blank=True,null=True)
#     family_sib2relation = models.TextField(default=None,blank=True,null=True)
#     family_sib2young = models.TextField(default=None,blank=True,null=True)
#     family_sib2occupations = models.TextField(default=None,blank=True,null=True)
#     family_sib2martial = models.TextField(default=None,blank=True,null=True)
#     family_sib2email = models.TextField(default=None,blank=True,null=True)
#     family_sib2dob = models.TextField(default=None,blank=True,null=True)
#     family_about_candidate = models.TextField(default=None,blank=True,null=True)
#     family_current_status = models.TextField(default=None,blank=True,null=True)

#     #Contact Details
#     contact_fathername = models.TextField(default=None,blank=True,null=True)
#     contact_street = models.TextField(default=None,blank=True,null=True)
#     contact_zipcode = models.TextField(default=None,blank=True,null=True)
#     contact_country = models.TextField(default=None,blank=True,null=True)
#     contact_city = models.TextField(default=None,blank=True,null=True)

#     contact_fatherhousename = models.TextField(default=None,blank=True,null=True)
#     contact_motherhousename = models.TextField(default=None,blank=True,null=True)
#     contact_mailid = models.TextField(default=None,blank=True,null=True)
#     contact_phonenum = models.TextField(default=None,blank=True,null=True)
#     contact_whatsappnum = models.TextField(default=None,blank=True,null=True)

#     contact_facebookurl = models.TextField(default=None,blank=True,null=True)
#     contact_linkurl = models.TextField(default=None,blank=True,null=True)
#     contact_instagramurl = models.TextField(default=None,blank=True,null=True)
#     contact_youtubeurl = models.TextField(default=None,blank=True,null=True)
#     contact_twitterurl = models.TextField(default=None,blank=True,null=True)
#     contact_websiteurl = models.TextField(default=None,blank=True,null=True)


#     # primary_details

#     marital_status =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     physical_mental_status =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     primary_email =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     primary_phone =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     primary_dob =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     Why_marry =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     behind_the_decision =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     school =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     school_year =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     major =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     are_you_working_non =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     company_name =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     position =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     salary_range =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     your_interest =   models.TextField(default=None, blank=True, null=True,max_length=500)
#     not_interest =   models.TextField(default=None, blank=True, null=True,max_length=500)
#     complexion = models.TextField(default=None, blank=True, null=True,max_length=500)
#     food_taste = models.TextField(default=None, blank=True, null=True,max_length=500)
#     opinion_diet = models.TextField(default=None, blank=True, null=True,max_length=500)
#     carrying_marriage = models.TextField(default=None, blank=True, null=True,max_length=500)
#     tobacco_product = models.TextField(default=None, blank=True, null=True,max_length=500)
#     consume_alcohol = models.TextField(default=None, blank=True, null=True,max_length=500)
#     illegal_drugs = models.TextField(default=None, blank=True, null=True,max_length=500)
#     criminal_offences = models.TextField(default=None, blank=True, null=True,max_length=500)
#     primary_options_country = models.TextField(default=None, blank=True, null=True,max_length=500)
#     selfie = models.FileField(upload_to = 'head_size',default=None, blank=True, null=True,max_length=500)
#     fullsize_img = models.FileField(upload_to = 'Full_size',default=None, blank=True, null=True,max_length=500)
#     family = models.FileField(upload_to = 'Family',default=None, blank=True, null=True,max_length=500)
#     gallery = models.FileField(upload_to = 'gallery',default=None, blank=True, null=True,max_length=500)
#     horoscope = models.FileField(upload_to = 'horoscope',default=None, blank=True, null=True,max_length=500)
#     profile_tag = models.TextField(default=None, blank=True, null=True,max_length=500)
#     treet_mypartner = models.TextField(default=None, blank=True, null=True,max_length=500)
#     treet_their_side = models.TextField(default=None, blank=True, null=True,max_length=500)
#     orphan = models.TextField(default=None, blank=True, null=True,max_length=500)
#     are_you_disable = models.TextField(default=None, blank=True, null=True,max_length=500)
#     which_organ = models.TextField(default=None, blank=True, null=True,max_length=500)
#     your_interest_choose = models.TextField(default=None, blank=True, null=True,max_length=500)
#     not_interest_choose = models.TextField(default=None, blank=True, null=True,max_length=500)
#     Course =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     Course1 =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     school1 =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     school_year1 =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     major1 =  models.TextField(default=None, blank=True, null=True,max_length=500)
#     food_taste_option = models.TextField(default=None, blank=True, null=True,max_length=500)
#     name = models.TextField(default=None, blank=True, null=True,max_length=500)
#     address = models.TextField(default=None, blank=True, null=True,max_length=500)
#     aadhar = models.TextField(default=None, blank=True, null=True,max_length=500)
#     gender = models.TextField(default=None, blank=True, null=True,max_length=500)
#     district = models.TextField(default=None, blank=True, null=True,max_length=500)
#     pincode = models.TextField(default=None, blank=True, null=True,max_length=500)

#     nameo = models.TextField(default=None, blank=True, null=True,max_length=500)
#     father_nameo = models.TextField(default=None, blank=True, null=True,max_length=500)
#     addresso = models.TextField(default=None, blank=True, null=True,max_length=500)
#     aadharo = models.TextField(default=None, blank=True, null=True,max_length=500)
#     gendero = models.TextField(default=None, blank=True, null=True,max_length=500)
#     districto = models.TextField(default=None, blank=True, null=True,max_length=500)
#     pincodeo = models.TextField(default=None, blank=True, null=True,max_length=500)
#     dobo = models.TextField(default=None, blank=True, null=True,max_length=500)
#     profileforwho = models.TextField(default=None, blank=True, null=True,max_length=500)
#     religion = models.TextField(default=None, blank=True, null=True,max_length=500)
#     age = models.TextField(default=None, blank=True, null=True,max_length=500)
#     family_fatherfamilyname = models.TextField(default=None, blank=True, null=True,max_length=500)
#     family_motherfamilyname = models.TextField(default=None, blank=True, null=True,max_length=500)


#     company_name1 = models.TextField(default=None, blank=True, null=True,max_length=500)
#     position1 = models.TextField(default=None, blank=True, null=True,max_length=500)
#     salary_range1 = models.TextField(default=None, blank=True, null=True,max_length=500)

#     profile_visibility = models.TextField(default=None, blank=True, null=True,max_length=500)


#     # hilight profile 

#     country_multiple = models.TextField(default=None, blank=True, null=True,max_length=500)
#     state_multiple = models.TextField(default=None, blank=True, null=True,max_length=500)
#     district_multiple = models.TextField(default=None, blank=True, null=True,max_length=500)
#     gender_multiple = models.TextField(default=None, blank=True, null=True,max_length=500)
#     languages_multiple = models.TextField(default=None, blank=True, null=True,max_length=500)
#     age_group = models.TextField(default=None, blank=True, null=True,max_length=500)
#     total_Number_of_Views = models.TextField(default=None, blank=True, null=True,max_length=500)
#     how_many_days_required = models.TextField(default=None, blank=True, null=True,max_length=500)
#     how_many_times_Repeat_per_day = models.TextField(default=None, blank=True, null=True,max_length=500)
#     block_list = models.TextField(default=None, blank=True, null=True,max_length=500)


# class countries(models.Model):
#     countryCode = models.TextField()
#     name = models.TextField()


# class states(models.Model):
#     name = models.TextField()
#     country_id = models.TextField()


# class cities(models.Model):
#     city = models.TextField()
#     state_id = models.TextField()

# class profile_finder_new(models.Model):
#     email = models.TextField()
#     mobile = models.IntegerField()
#     password = models.TextField()
#     confirm_password = models.TextField()
#     referral_code = models.CharField(default=None, blank=True, null=True,max_length=6)
#     code = models.CharField(default=None, blank=True, null=True,max_length=6)



# class follow_request(models.Model):
#     sender_id = models.IntegerField(default=None, blank=True, null=True)
#     receiver_id = models.IntegerField(default=None, blank=True, null=True,)
#     accept = models.TextField(default=None, blank=True, null=True,max_length=10)
#     name = models.TextField(default=None, blank=True, null=True,max_length=10000)
#     place = models.TextField(default=None, blank=True, null=True,max_length=10000)




# class upload(models.Model):
#     useremail = models.CharField(max_length=30,null=True)
#     fullname = models.CharField(max_length=30,null=True)
#     date_of_marriage = models.CharField(max_length=30,null=True)
#     words_about_marrio = models.CharField(max_length=300,null=True)
#     marriage_photos = models.ImageField(upload_to='media/happycoupls',default="")
#     # marriage_photos = models.TextField(null=True)