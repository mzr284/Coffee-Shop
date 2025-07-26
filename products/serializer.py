from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id", "category", "title", "count", "avatar", "description", "is_enable"]

    def get_category(self, obj):
        return obj.category.title


class CategorySerialize(serializers.ModelSerializer):

    parent = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "parent", "title", "avatar", "products"]

    def get_parent(self, obj):
        if obj.parent:
            return obj.parent.title

