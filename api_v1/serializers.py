from rest_framework import serializers
from .models import Author, Category, Publisher, Book, Reader, BookCard, BookCardItem


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'full_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), source='publisher', write_only=True
    )
    authors = AuthorSerializer(read_only=True, many=True)
    author_ids = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='authors', write_only=True, many=True
    )
    categories = CategorySerializer(read_only=True, many=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='categories', write_only=True, many=True
    )

    class Meta:
        model = Book
        fields = [
            'id', 'isbn', 'title', 'year_published', 'description',
            'total_copies', 'available_copies', 'added_date',
            'publisher_name', 'publisher_id',
            'authors', 'author_ids',
            'categories', 'category_ids',
        ]


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'


class BookCardItemSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book', write_only=True
    )
    reader_name = serializers.CharField(source='book_card.reader.full_name', read_only=True)
    library_card_number = serializers.CharField(source='book_card.reader.library_card_number', read_only=True)

    class Meta:
        model = BookCardItem
        fields = [
            'id', 'book_title', 'book_id', 'reader_name', 'library_card_number',
            'issue_date', 'due_date', 'return_date', 'status', 'notes',
        ]


class BookCardSerializer(serializers.ModelSerializer):
    reader = ReaderSerializer(read_only=True)
    items = BookCardItemSerializer(many=True, read_only=True)

    class Meta:
        model = BookCard
        fields = ['id', 'reader', 'created_date', 'is_active', 'items']