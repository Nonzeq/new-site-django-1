from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', GamesHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('Hide/', Hide.as_view(), name='Hide'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', Games_show_catogory.as_view(), name='category'),
    path('comments/<int:pk>/', Comment_show.as_view(), name='Comment_show'),
]

