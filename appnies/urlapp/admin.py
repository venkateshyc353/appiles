from django.contrib import admin
from . models import url_model

class url_admin(admin.ModelAdmin):
    list_display = ['url','empolyer'
                    ]
admin.site.register(url_model,url_admin)
# Register your models here.
