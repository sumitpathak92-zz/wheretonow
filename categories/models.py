from django.db import models

class Categories(models.Model):
    category_type = models.CharField(max_length=20, blank=False)
    brief_desc = models.TextField(max_length=100, blank=False)
    google_category_code = models.CharField(max_length=20, blank=False, default='google_place_code')

    def __str__(self):
        return self.category_type

    class Meta:
        db_table='wheretonow_place_categories'
        ordering = ('category_type',)

