from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

class ProductView(APIView):

    def get(self , request , format=None):
        all_products = Product.objects.all().order_by('-id')
        serializer = ProductSerializer(all_products , many=True)
        return Response({'ok': True , 'data': serializer.data}, status=200)

    def post(self , request , format=None):
        request_data = JSONParser().parse(request)
        serializer = ProductSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data})
        return Response({'ok': False , 'message': 'Something went wrong' , 'error': serializer.errors})
        

    def patch(self , request , format=None):
        request_data = JSONParser().parse(request)
        product_instance = Product.objects.get(id=request_data['id'])
        serializer = ProductSerializer(product_instance ,data=request_data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data})
        return Response({'ok': False , 'message': 'Something went wrong' , 'error': serializer.errors})
        
    def delete(self , request, format=None):
        request_data = JSONParser().parse(request)
        try:
            object_instance = Product.objects.get(id=request_data['id'])
            object_instance.delete()
            return Response({'ok': True , 'message': 'Deleted!' , 'product': request_data})
        except:
            return Response("Not Found!")
        
