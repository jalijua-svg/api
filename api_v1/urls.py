from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet, CategoryViewSet, PublisherViewSet,
    BookViewSet, ReaderViewSet, BookCardViewSet, BookCardItemViewSet,
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'books', BookViewSet)
router.register(r'readers', ReaderViewSet)
router.register(r'bookcards', BookCardViewSet)
router.register(r'bookcarditems', BookCardItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]