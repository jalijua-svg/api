from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_extensions.cache.decorators import cache_response
from . import models
from . import serializers


class AuthorViewSet(viewsets.ModelViewSet):
    """Представление для работы с авторами."""
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(full_name__icontains=name)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Author.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Author.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    """Представление для работы с категориями."""
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Category.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Category.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherViewSet(viewsets.ModelViewSet):
    """Представление для работы с издательствами."""
    serializer_class = serializers.PublisherSerializer
    queryset = models.Publisher.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Publisher.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Publisher.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookViewSet(viewsets.ModelViewSet):
    """Представление для работы с книгами."""
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.query_params.get('title')
        author_id = self.request.query_params.get('author_id')
        category_id = self.request.query_params.get('category_id')
        publisher_id = self.request.query_params.get('publisher_id')
        if title:
            qs = qs.filter(title__icontains=title)
        if author_id:
            qs = qs.filter(authors__id=author_id)
        if category_id:
            qs = qs.filter(categories__id=category_id)
        if publisher_id:
            qs = qs.filter(publisher_id=publisher_id)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Book.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Book.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReaderViewSet(viewsets.ModelViewSet):
    """Представление для работы с читателями."""
    serializer_class = serializers.ReaderSerializer
    queryset = models.Reader.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        card = self.request.query_params.get('library_card_number')
        if name:
            qs = qs.filter(full_name__icontains=name)
        if card:
            qs = qs.filter(library_card_number__icontains=card)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Reader.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.Reader.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookCardViewSet(viewsets.ModelViewSet):
    """Представление для работы с книжными карточками."""
    serializer_class = serializers.BookCardSerializer
    queryset = models.BookCard.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        reader_id = self.request.query_params.get('reader_id')
        if reader_id:
            qs = qs.filter(reader_id=reader_id)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.BookCard.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.BookCard.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookCardItemViewSet(viewsets.ModelViewSet):
    """Представление для работы с записями выдачи книг."""
    serializer_class = serializers.BookCardItemSerializer
    queryset = models.BookCardItem.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        book_card_id = self.request.query_params.get('book_card_id')
        book_id = self.request.query_params.get('book_id')
        status_filter = self.request.query_params.get('status')
        if book_card_id:
            qs = qs.filter(book_card_id=book_card_id)
        if book_id:
            qs = qs.filter(book_id=book_id)
        if status_filter:
            qs = qs.filter(status=status_filter)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.BookCardItem.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [models.BookCardItem.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)