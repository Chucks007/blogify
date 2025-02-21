from django.contrib import admin
from . import models

admin.site.site_header = 'AlienCode Admin'
admin.site.site_title = 'AlienCode Admin Panel'
admin.site.index_title = 'Welcome to AlienCode Admin Panel'

# Register your models here.
admin.site.register((models.Blog, models.BlogComment))
admin.site.register(models.ViewsModel)
admin.site.register(models.Profile)
admin.site.register(models.Contact)
admin.site.register(models.Subscription)
