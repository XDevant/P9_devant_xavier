from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import review.views
import authentication.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('flux/', review.views.flux, name='flux'),
    path('posts/', review.views.posts, name='posts'),
    path('ticket/add/',review. views.create_ticket, name='create-ticket'),
    path('review/add/',review. views.create_review, name='create-review'),
    path('post/add/',review. views.create_post, name='create-post'),
    path('followed/', review.views.followed, name='followed'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
