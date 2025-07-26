from django.contrib import admin

from .models import Product, Category


class ProductInlineAdmin(admin.StackedInline):
    model = Product
    fields = ["id", "title", "count", "avatar", "description", "is_enable",]
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "avatar", "parent"]
    list_filter = ["parent"]
    search_fields = ["title"]
    inlines = [ProductInlineAdmin]


