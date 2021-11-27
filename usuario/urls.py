from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('',views.base_view),
    path('Create',views.addCLiente.as_view()),

]
