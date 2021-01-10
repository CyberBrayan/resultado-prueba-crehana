from django.contrib import admin
from crehana.curso.models import Category,Course

class CategoryAdmin(admin.ModelAdmin):

    fields = ('name',)

    list_display=("name",)

    search_fields=("name",)

    list_per_page = 10

class CourseAdmin(admin.ModelAdmin):

    fields = ('title','category',)

    list_display=("title",'category')

    search_fields=("title",)

    list_per_page = 10

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)