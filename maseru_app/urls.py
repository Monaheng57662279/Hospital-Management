from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowStaff, name='show_staff'),
    path('insertstaff', views.InsertStaff, name='Insertstaff'),
    path('editstaff/<int:id>', views.EditStaff, name="edit_staff"),
    path('updatestaff/<int:id>', views.UpdateStaff, name="update_staff"),
    path('deletestaff/<int:id>/', views.DeleStaff, name='delete_staff'),
]