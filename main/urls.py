from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    # # login the user /login/
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register', register, name="register"),
    # path('accounts/profile/', profile, name="profile"),
    # path('post/<slug>/', post, name = 'post'),
    # path('about/', about,name = 'about' ),
    # path('postlist/<slug>/', postlist, name = 'postlist'),
    # path('posts/', allposts, name = 'allposts'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)