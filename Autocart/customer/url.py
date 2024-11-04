from django.conf.urls import url
from customer import views


urlpatterns = [
    url('customer/', views.customer)
]