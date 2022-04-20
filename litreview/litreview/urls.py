from django.contrib import admin
from django.urls import path
import  review.views
import authentication.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('flux/', review.views.flux, name='flux'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
]
