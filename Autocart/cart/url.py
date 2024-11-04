from django.conf.urls import url
from cart import views
from django.urls import path


urlpatterns = [
    url('cart/', views.viewcart),
    path('checkout/', views.checkout_view, name='checkout_action_url'),
]