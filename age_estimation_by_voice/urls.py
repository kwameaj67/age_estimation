from django.contrib import admin
from django.urls import path
# import the view function from views.py
from .views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
   # 8. add this 
    path('',hello_world,name="hello_world") 
    # path (url here, view here, name of path here (can be anything))
]
