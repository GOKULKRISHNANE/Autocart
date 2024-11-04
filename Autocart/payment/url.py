from django.conf.urls import url
from payment import views

urlpatterns = [
    url('payment/', views.add_payment),
    url('view_pay/', views.view_payment)

]

