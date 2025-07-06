from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('mystery', 'Mystery'),
        ('sci-fi', 'Sci-Fi'),
        ('biography', 'Biography'),
        ('fantasy', 'Fantasy'),
        ('romance', 'Romance'),
        ('history', 'History'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.TextField(blank=True)

    # 🆕 New fields with safe defaults
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='other')
    rating = models.IntegerField(default=3)

    def __str__(self):
        return self.title
