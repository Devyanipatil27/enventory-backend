from django.urls import path
from .views import ItemCreateView, ItemRetrieveView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/', ItemRetrieveView.as_view(), name='item-detail'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]
