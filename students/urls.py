from django.urls import path
from .views import student_add_update, student_delete, student_list


urlpatterns = [
    path('', student_add_update, name='home'),
    path('list/', student_list, name='list'),
    path('<int:id>/', student_add_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),

]