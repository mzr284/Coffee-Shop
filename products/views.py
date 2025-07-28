from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product
from .serializer import CategorySerialize, ProductSerializer



class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        print(request.auth)
        categories = Category.objects.all()
        serialzer = CategorySerialize(categories, many=True, context={'request': request})
        return Response(serialzer.data)

    def post(self, request):
        serial = CategorySerialize(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)




class CategoryDetailView(APIView):

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return category

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerialize(category, context={'request': request})
        return Response(serializer.data)

    def put(self, requset, pk):
        category = self.get_object(pk)
        serial = CategorySerialize(category, data=requset.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk):
        category = self.get_object(pk)
        category.delete()
        return Response({"here we go!!!": "Delete mission successfully!"}, status=status.HTTP_204_NO_CONTENT)


# class CategoryView(viewsets.ModelViewSet):
#     query_set = Category.objects.all()
#     serializer_class = CategorySerialize


class ProductListView(APIView):

    def get(self, request, pk_category):
        products = Product.objects.filter(category=pk_category)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, title_category, pk_product):
        product = Product.objects.get(pk=pk_product, category__title=title_category)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)