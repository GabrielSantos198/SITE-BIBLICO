from django.contrib import admin
from . models import Post

# Register your models here.
@admin.register(Post)
class admin(admin.ModelAdmin):
    list_display = ('titulo','slug','criado','atualizado')
    search_fields = ('titulo','sumario')
    prepopulated_fields = {'slug': ('titulo',)}
