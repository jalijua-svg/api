from django.contrib import admin
from .models import Author, Category, Publisher, Book, Reader, BookCard, BookCardItem

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    search_fields = ['full_name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'total_copies', 'available_copies', 'added_date']
    search_fields = ['title', 'isbn']

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'library_card_number', 'is_blocked', 'registration_date']
    search_fields = ['full_name', 'library_card_number']

@admin.register(BookCard)
class BookCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'reader', 'created_date', 'is_active']

@admin.register(BookCardItem)
class BookCardItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_card', 'book', 'issue_date', 'due_date', 'status']
    list_filter = ['status']