from rest_framework import serializers

from .models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "pk",
            "name",
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "pk",
            "image",
        )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "price",
            "discount",
            "favorite",
            "preview",
            "category",
            "images",
        )
