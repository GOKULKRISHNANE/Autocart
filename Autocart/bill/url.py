from django.conf.urls import url
from bill import views


urlpatterns = [
    url('admin/', views.view_bill_admin),
    url('staff/', views.view_bill_staff),
    url('customer/', views.view_bill_customer),



]
