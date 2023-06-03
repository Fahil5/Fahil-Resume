from django.urls import path
from . import views
app_name='cvapp'
urlpatterns = [
    path('page',views.page,name="page"),
]