from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.render_mainpage),
    url(r'^get_input$', views.get_input),
    url(r'^measure_speed\/$', views.measure_speed),
]