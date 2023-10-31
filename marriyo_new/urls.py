from django.urls import path
from profile_finder import views
from private_investigator import pi_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainpage),
    path('dashboard', views.profile_dashboard),
    path('signin', views.signin),
    path('signup', views.signup),
    path('profile_manager_list/<id>', views.profile_manager_list),
    path('private_investigator_list/<id>', views.private_investigator_list),
    path('statelist/<int:pk>/',views.statelist),
    path('rstatelist/<int:pk>/',views.rstatelist),
    path('fstatelist/<int:pk>/',views.fstatelist),
    path('mstatelist/<int:pk>/',views.mstatelist),
    path('ccstatelist/<int:pk>/',views.ccstatelist),
    path('citylist/<int:pk>/',views.citylist),
    path('rcitylist/<int:pk>/',views.rcitylist),
    path('citylistp/<int:pk>/',views.citylistp),
    path('otp/<id>', views.opt_check),
    # path('dashboard/<id>', views.profile_dashboard),
    path('profileidcard/<id>', views.profileidcard),
    path('profileforwhom/<id>', views.profileforwhom),
    path('profileform/<id>', views.profileform),
    #path('profilepicture', views.profilepicture),
    path('selfie_upload/<id>',views.selfie_upload),
    path('primary_details/<id>', views.primary_details),
    path('family_details/<id>',views.family_details),
    path('contact_details/<id>',views.contact_details),
    path('header/<id>',views.header),
    path('profile_page/<id>',views.profile_page),
    path('menu_header',views.menu_header),
    path('highlight_profile/<id>',views.highlight_profile),
    path('highlight_payment/<id>',views.highlight_payment),
    path('payment',views.payment),
    path('matching_list/<id>',views.matching_list),
    path('viewallmatch/<id>',views.viewallmatch),
    path('package_matching/<id>',views.package_matching),
    path('requested_list/<id>',views.requested_list),
    path('received/<id>',views.received),
    path('saved_Search/<id>',views.saved_search),
    path('saved_search_view_profile/<uid>/<id>',views.saved_search_view_profile),
    path('request_received',views.follow_request1),
    path('sucess_story',views.happy_couples),
    path('hai',views.test2),
    #favorites
    path('myfavorites/<id>',views.myfavorites),
    path('favorites_to_me/<id>',views.favorites_to_me),
    #happy Couple
    path('happycouples/<id>', views.happycouple),
    path('success_story/<id>', views.success_Story),
    # path('uploadyours/', views.uploadyours),
    path('package/<id>', views.package),
    path('package_amount/<id>', views.package_amount),
    path('happy_couples_upload/<id>', views.happy_couples_upload),

    # path('happycouples1/', views.happycouples1),
    path('happy_couples_test', views.happy_couples_test),
    #block
    path('Block', views.block),
    #settings
    path('settings_notification/<id>', views.settings_notification),
    path('settings_privacy/<id>', views.settings_privacy),
    path('settings_security/<id>', views.settings_security),
    path('settings_subscription/<id>', views.settings_subscription),
    path('settings_wallet/<id>', views.settings_wallet),
    path('settings_about/<id>', views.settings_about),
    path('wallet_add/<id>', views.wallet_add),
    path('muted_acc/<id>', views.muted_acc),
    path('blocked_acc/<id>', views.blocked_acc),

    #private investigator
    path('all_investigator/<id>', views.all_investigator),
    path('hire_investigator/<id>', views.hire_investigator),
    path('my_investigator/<id>', views.my_investigator),
    path('my_investigator_question/<id>', views.my_investigator_question),
    path('pi_payment/<id>', views.pi_payment),






#///////////////////private investagator////////////////////
    path('pi_signin', pi_views.signin),
    path('pi_signup', pi_views.signup),
    path('pi_otpcheck/<id>', pi_views.opt_check),
    path('pi_profilepicture/<id>', pi_views.profile_picture),
    path('pi_complete_profile/<id>', pi_views.complete_profile),
    path('pi_admin_dashboard/<id>', pi_views.admin_dashboard),
    path('pi_profile/<id>', pi_views.profile),
    path('edit_profile/<id>', pi_views.edit_profile),
    path('pi_payment_screen/<id>', pi_views.payment),
    path('pi_client_list/<id>', pi_views.client_list),
    path('pi_client_details/<id>', pi_views.client_details),
    path('pi_subscription/<id>', pi_views.subscription),
    path('pi_payment_table/<id>', pi_views.payment_table),
    path('pi_add_client/<id>', pi_views.add_client),
    path('pi_client_feedback/<id>', pi_views.client_feedback),
    path('pi_setting/<id>', pi_views.setting),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)