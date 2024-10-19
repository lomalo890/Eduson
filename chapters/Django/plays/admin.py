from django.contrib import admin
from plays.models import Play, Actor, Show

class ShowAdminInline(admin.TabularInline):
    model = Show
    extra = 0 # чтобы мы могли занести только одну дату, а не несколько для одной постановки

class PlayAdmin(admin.ModelAdmin):
    list_display=('title',)
    inlines = [ShowAdminInline]

class ShowAdmin(admin.ModelAdmin):
    list_display = ("play_name", "start_at",)


# Register your models here
admin.site.register(Play, PlayAdmin)
admin.site.register(Actor, admin.ModelAdmin)
admin.site.register(Show, ShowAdmin)
