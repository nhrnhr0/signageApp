from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
# Create your views here.


def partial_barcode_to_regex_pattern(barcode):
    pattern = barcode.replace(" ", r"\d")
    return pattern + r"\d*"


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_product_view(request, barcode):
    pattern = partial_barcode_to_regex_pattern(barcode)
    product = Product.objects.filter(barcode__iregex=pattern).first()
    if not product:
        return Response({'error': 'Product not found'}, status=404)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
