from django.urls import  path

from . import views



urlpatterns = [
    path('telegram/geturi/<int:telId>',views.geturiTelegram,name='geturi'),
    path('telegram/addnewuser/<int:telId>/<int:userCount>/',views.addTelegramUseer,name='addTelegramUseer'),
    path('telegram/deluri/<str:domain>/',views.deluri,name='deluri'),

    
    


]


