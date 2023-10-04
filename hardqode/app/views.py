from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import models
from app.models import LessonView, Product
from app.serializers import LessonViewSerializer, ProductSerializer

class LessonListView(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return LessonView.objects.filter(user=user)


class ProductLessonListView(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return LessonView.objects.filter(user=user, lesson__products__id=product_id)

class ProductStatsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.all()

        stats = []
        for product in products:
            lesson_views = LessonView.objects.filter(user=user, lesson__products=product)
            total_views = lesson_views.count()
            total_time = lesson_views.aggregate(total_time=models.Sum('view_time_seconds'))['total_time']
            student_count = lesson_views.values('user').distinct().count()
            access_count = product.lesson_set.count()

            purchase_percent = (access_count / user.objects.count()) * 100

            stats.append({
                'product_id': product.id,
                'product_name': product.name,
                'total_views': total_views,
                'total_time': total_time,
                'student_count': student_count,
                'purchase_percent': purchase_percent
            })

        return stats
