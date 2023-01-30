from django.contrib import admin
from .models import Todo, User, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Todo)