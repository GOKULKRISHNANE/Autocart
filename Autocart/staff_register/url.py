from django.conf.urls import url
from staff_register import views


urlpatterns = [
    url('staff_register/', views.staff_register),
    url('update_profile/(?P<idd>\w+)', views.update_profile),
    url('view_updateprofile/', views.view_updatedprofile),
    url('delete/(?P<idd>\w+)', views.delete)



]