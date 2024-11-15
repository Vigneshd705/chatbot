from django.urls import path
from .views import chatbotResponse
urlpatterns = [
    # path('OnelifeChatbot/', chatbotResponse, name='chatBotResponse'),
    path('api1/',chatbotResponse,name='chatbotResponse'),
]