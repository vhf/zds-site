from django.contrib import admin

from zds.utils.models import Alert, License, Category, SubCategory, CategorySubCategory, Tag, HelpWriting


class SubCategoryAdmin(admin.ModelAdmin):

    def parent_category(self, obj):
        return obj.get_parent_category()

    parent_category.admin_order_field = 'categorysubcategory__category'
    parent_category.short_description = 'Parent category'

    list_display = ('parent_category', 'title', 'subtitle')
    ordering = ('categorysubcategory__category', 'title')


admin.site.register(Alert)
admin.site.register(Tag)
admin.site.register(License)
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CategorySubCategory)
admin.site.register(HelpWriting)
