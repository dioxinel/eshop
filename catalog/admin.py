from django.contrib import admin
from .models import *


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0


class SectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Section._meta.fields]
    inlines = [CategoryInline]

    class Meta:
        model = Section

admin.site.register(Section, SectionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    inlines = [SubcategoryInline]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subcategory._meta.fields]

    class Meta:
        model = Subcategory

admin.site.register(Subcategory, SubcategoryAdmin)
