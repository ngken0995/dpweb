from django.contrib import admin
from .models import Happiness, User, Article, Calorie, Personal, Favorite
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Calorie)
class CalorieAdmin(ImportExportModelAdmin):
    list_display = ("sedentary", "moderatelyActive", "active", "age", "gender")
    pass

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)

admin.site.register(User)
admin.site.register(Personal)
admin.site.register(Article)
admin.site.register(Happiness,RatingAdmin)
admin.site.register(Favorite)