from django.urls import path
from .import views
urlpatterns = [
    # path('',views.Home, name="home"),
    path('ajexdata',views.Ajexdata, name="ajexdata"),
    path('',views.Showalldata, name="showalldata"),
    path('delete_data', views.Deletedata, name='delete_data'),
    path('edit_data', views.Editdata, name='edit_data'),
]