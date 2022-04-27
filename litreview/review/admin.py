from django.contrib import admin
from review.models import Ticket, Review, UserFollows

admin.site.register([Ticket, Review, UserFollows])
