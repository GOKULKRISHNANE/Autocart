from django.conf.urls import url
from feedback import views


urlpatterns = [
    url('add_feedback/', views.add_feedback),
    url('view_feedback_staff/', views.view_feedback_staff),
    url('view_feed_adm', views.view_feedback_admin)


]





