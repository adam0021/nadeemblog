from django.contrib import admin
from blog.models import Post,comment

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display=['title','timestamp','updated']
    list_display_links=['updated']
    list_filter=['updated','timestamp']
    search_fields=['title','content']
    list_editable=['title']
    class Meta:
        model=Post





admin.site.register(Post,PostModelAdmin)
admin.site.register(comment)