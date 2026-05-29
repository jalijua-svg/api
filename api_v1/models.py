from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    isbn = models.CharField(max_length=20, unique=True, null=True, blank=True)
    title = models.CharField(max_length=300)
    year_published = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    added_date = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField(Author, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title


class Reader(models.Model):
    library_card_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    is_blocked = models.BooleanField(default=False)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} ({self.library_card_number})'


class BookCard(models.Model):
    reader = models.OneToOneField(Reader, on_delete=models.CASCADE, related_name='book_card')
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Карточка {self.reader}'


class BookCardItem(models.Model):
    STATUS_CHOICES = [
        ('Выдана', 'Выдана'),
        ('Продлена', 'Продлена'),
        ('Возвращена', 'Возвращена'),
        ('Просрочена', 'Просрочена'),
    ]
    book_card = models.ForeignKey(BookCard, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Выдана')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.book.title} - {self.book_card.reader}'