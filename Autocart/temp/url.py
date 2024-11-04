from django.conf.urls import url
from temp import views
urlpatterns = [
    url('admin/',views.admin),
    url('customer/',views.customer),
    url('home/',views.home),
    url('staff/',views.staff)



            ]
