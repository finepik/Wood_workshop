from django.contrib import admin

from .models import Product, ProductImage, Category, Proposal


class ProductInline(admin.StackedInline):
    model = ProductImage
    verbose_name = "Файл с изображением"
    verbose_name_plural = "Все фото изделия"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "name", "description_short", "price", "discount", "favorite"
    list_display_links = ("name",)
    search_fields = "name", "favorite"

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:45] + "..."

    description_short.short_description = "Краткое описание"


admin.site.register(Category)


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = "customer_name", "phone_number", "description_short"
    list_display_links = ("customer_name",)

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:45] + "..."

    description_short.short_description = "Пожелания"
