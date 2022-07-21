from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Products

def validate_title(value):
    qs=Products.objects.filter(title__iexact=value)
    print(qs)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name.")
    return value

def validate_title_on_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"hello is not allowed")

unique_product_title=UniqueValidator(queryset=Products.objects.all(),lookup='iexact')
