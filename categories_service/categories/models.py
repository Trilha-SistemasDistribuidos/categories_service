from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    recommended_for = models.CharField(
        max_length=20,
        choices=[
            ('family', 'Família'),
            ('adventurer', 'Aventureiro'),
            ('couples', 'Casais'),
            ('seniors', 'Idosos'),
            ('nature_lovers', 'Amantes da Natureza'),
        ],
        default='family'
    )

    def __str__(self):
        return self.name
