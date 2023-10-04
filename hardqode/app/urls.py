from django.urls import path
from app.views import (
    LessonListView,
    ProductLessonListView,
    ProductStatsView,
)

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('products/<int:product_id>/lessons/',
         ProductLessonListView.as_view(), name='product-lesson-list'),
    path('product-stats/', ProductStatsView.as_view(), name='product-stats'),
]

