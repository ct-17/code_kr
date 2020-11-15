from django.urls import path
from . import views

urlpatterns = [
    # list merchant profile
    path('merchantprofilemanagement/get_table_merchant_profile', views.get_table_merchant_profile),
    path('merchantprofilemanagement/search_table_merchant_profile', views.search_table_merchant_profile),
    path('merchantprofilemanagement/get_combobox_language', views.get_combobox_language),
    path('merchantprofilemanagement/delete_merchant_profile', views.delete_merchant_profile),
    # module create merchant profile
    path('merchantprofilemanagement/init_create_profile_information', views.init_create_profile_information),
    path('merchantprofilemanagement/create_profile_information', views.create_profile_information),
    # module create merchant profile
    path('merchantprofilemanagement/init_profile_information_detail', views.init_profile_information_detail)
    ]