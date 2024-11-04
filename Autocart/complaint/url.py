from django.conf.urls import url
from complaint import views


urlpatterns = [
    url('addcomplaint/', views.add_complaint),
    url('post_replay/(?P<idd>\w+)', views.post_replay),
    url('view_cmp/', views.view_complaint),
    url('view_replay/', views.view_replay)


]



