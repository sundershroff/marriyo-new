from django import forms
from .models import *

class ProfileSigninForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['email','password']

class ProfileFinderForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['email','mobile','password','confirm_password','referral_code','code','user_otp']


class ProfileOtpForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['user_otp']

class profileIdCardForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['idcard']



class profileForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = "__all__"
        # fields = ['name','address','height','weight','martial','physical','religion','age','birth_place','birth_country','birth_time','birth_city','orgin','r_country','r_state',
        #           'denomination','blood_group','r_status','temple_name','temple_street','temple_post_code','temple_city','temple_country','temple_phone_number','temple_diocese','temple_local_admin','emergency_name',
        #           'emergency_relation','emergency_phone_number','emergency_email','emergency_marital_status','emergency_occupations']
        

class profilepictureForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['profile_picture']



class family_detailsForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['family_status','family_fathername','family_fatherbirthcountry','family_fatherbirthcity',
                  'family_fatherjob','family_mothername','family_motherbirthcountry','family_motherbirthcity',
                  'family_motherjob','family_sib1name','family_sib1relation','family_sib1young','family_sib1occupations',
                  'family_sib1martial','family_sib1email','family_sib1dob','family_sib2name','family_sib2relation','family_sib2young',
                  'family_sib2occupations','family_sib2martial','family_sib2email','family_sib2dob','family_about_candidate',
                  'family_current_status']


class contact_detailsForm(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['contact_fathername','contact_street','contact_zipcode',
                  'contact_country','contact_city','contact_fatherhousename',
                  'contact_motherhousename','contact_mailid','contact_phonenum',
                  'contact_whatsappnum','contact_facebookurl','contact_linkurl',
                  'contact_instagramurl','contact_youtubeurl','contact_twitterurl','contact_websiteurl']
        

class Primary_details(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['marital_status','physical_mental_status','primary_email',
                  'primary_phone','primary_dob','Why_marry','behind_the_decision',
                  'school','school_year','major','are_you_working_non','company_name',
                  'position','salary_range','your_interest','not_interest','complexion',
                  'food_taste','opinion_diet','carrying_marriage','tobacco_product',
                  'consume_alcohol','illegal_drugs','criminal_offences','primary_options_country',
                  'selfie','fullsize_img','family','gallery','horoscope','profile_tag',
                  'treet_mypartner','treet_their_side','orphan','are_you_disable',
                  'which_organ','your_interest_choose','not_interest_choose','Course',
                  'Course1','school1','school_year1','major1','food_taste_option']
        

class Aboutme_Form(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['family_about_candidate']


class Currentstatus_Form(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['family_current_status']


class Contact_Form(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['address','addresso','primary_phone','primary_email']


class Otherdetails_Form(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['primary_email','contact_phonenum','contact_whatsappnum']



class Highlight_Profile(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['country_multiple','state_multiple','district_multiple','gender_multiple','languages_multiple','age_group','total_Number_of_Views','how_many_days_required','how_many_times_Repeat_per_day']


class follow_requestForm(forms.ModelForm):
    class Meta:
        model = follow_request
        fields = ['receiver_id','sender_id','name','place']

# class request_Accept_Form(forms.ModelForm):
#     class Meta:
#         model = follow_request
#         fields = ['accept']


class Block(forms.ModelForm):
    class Meta:
        model = profile_finder
        fields = ['block_list']

class uploadone(forms.ModelForm):
    class Meta:
        model = upload
        fields = ['marriage_photos']