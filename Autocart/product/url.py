from django.conf.urls import url
from product import views


urlpatterns = [
    url('add_product/', views.add_product),
    url('view_product_cust/', views.view_product_customer),
    url('view_product/', views.view_product),
    url('view_product_adm/',views.view_product_admin)


]