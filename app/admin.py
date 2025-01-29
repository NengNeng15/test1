from django.contrib import admin
from .models import User, Venue, Lesson, Appointment, Payment

# Registering models to the admin site
admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Lesson)
admin.site.register(Appointment)
admin.site.register(Payment)
