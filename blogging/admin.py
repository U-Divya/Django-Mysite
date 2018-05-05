from django.contrib import admin

# Register your models here.
from .models import Blog,Other,Other1,Other2


class BlogAdmin(admin.ModelAdmin):
	list_display=['title','author','published']
	search_fields=['title']
	list_filter=['published']


admin.site.register(Blog,BlogAdmin)
admin.site.register(Other)
admin.site.register(Other1)
admin.site.register(Other2)
