from django.db import models

# Create your models here.

class PageText(models.Model):

    page_choice = (
        ('All Prducts', 'All Products'),
        ('Homeware', 'Homeware'),
        ('Accessories and Gifts', 'Accessories and Gifts'),
        ('Special Offers', 'Special Offers')
    )

    page = models.CharField(
        max_length=100,
        choices=page_choice,
        blank=True
        
    )

    page_text = models.TextField(blank=True)

    def __str__(self):
        return self.page


