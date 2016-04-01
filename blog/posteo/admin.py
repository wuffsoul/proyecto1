from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display=["titulo","estampaInicial","estampaActualizacion"]
    list_display_links=["estampaActualizacion"]
    list_filter=["estampaInicial","estampaActualizacion"]
    class Meta:
        model=Post

admin.site.register(Post,PostModelAdmin)
