from django.urls import  path

from . import views



urlpatterns = [
    path('geturi/',views.geturi,name='geturi'),
    path('telegram/geturi/<int:telId>',views.geturiTelegram,name='geturi'),
    path('telegram/addnewuser/<int:telId>/<int:userCount>/',views.addTelegramUseer,name='addTelegramUseer'),
    path('xuiRestart/',views.xuiRestart,name='xuiRestart'),
    
    


]


