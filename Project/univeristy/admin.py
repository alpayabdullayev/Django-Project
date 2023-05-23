from django.contrib import admin
from univeristy.models import*

# Register your models here.
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description')
    list_filter = ["title", "link"]
    search_fields = ('title', 'description')
    ordering=['id']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ["name"]
    search_fields = ('name',)
    ordering=['id']                                                                                                                                        
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)