from django.urls import path
from transfer.views import index,detail,update,thanks

app_name = 'transfer'

urlpatterns = [
    path('',index.as_view(), name = 'index'),
    path('preview/<int:pk>/',detail.as_view(), name = 'detail'),
    path('update/<int:pk>/',update.as_view(), name = 'update'),
    path('thanks/<int:pk>/',thanks,name = 'thanks'),
]