from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer
from rest_framework.exceptions import NotFound

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemRetrieveView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cached_item = cache.get(item_id)
        if cached_item:
            return Response(cached_item)

        try:
            item = self.get_object()
        except Item.DoesNotExist:
            raise NotFound("Item not found")
        
        cache.set(item_id, ItemSerializer(item).data)
        return super().get(request, *args, **kwargs)

class ItemUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]
