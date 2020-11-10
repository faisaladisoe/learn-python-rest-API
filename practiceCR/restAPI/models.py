from django.db import models

# Create your models here.
class Biodata(models.Model):
    nickname = models.CharField(max_length = 20, null = True)
    fullname = models.CharField(max_length = 100, null = True)
    CLASSROOM_CHOICES = (
        ('12 IPA 1', '12 IPA 1'),
        ('12 IPA 2', '12 IPA 2'),
        ('12 IPA 3', '12 IPA 3'),
        ('12 IPA 4', '12 IPA 4'),
        ('12 IPA 5', '12 IPA 5'),
        ('12 IPA 6', '12 IPA 6'),
        ('12 IPA 7', '12 IPA 7'),
        ('12 IPA 8', '12 IPA 8'),
        ('12 IPS', '12 IPS'),
    )
    classroom = models.CharField(
        max_length = 10,
        choices = CLASSROOM_CHOICES,
        default = '12 IPA 1',
        null = True
    )
    randomThought = models.CharField(max_length = 100, null = True)
    email = models.EmailField(max_length = 100, null = True)
    instagram = models.CharField(max_length = 50, null = True)
    linkedin = models.CharField(max_length = 50, null = True)

    def __str__(self):
        return self.fullname
    
class Layouting(models.Model):
    search = models.CharField(max_length = 50, null = True)
    GROUP_CHOICES = (
        ('All', 'All'),
        ('12 IPA 1', '12 IPA 1'),
        ('12 IPA 2', '12 IPA 2'),
        ('12 IPA 3', '12 IPA 3'),
        ('12 IPA 4', '12 IPA 4'),
        ('12 IPA 5', '12 IPA 5'),
        ('12 IPA 6', '12 IPA 6'),
        ('12 IPA 7', '12 IPA 7'),
        ('12 IPA 8', '12 IPA 8'),
        ('12 IPS', '12 IPS'),
    )
    groupby = models.CharField(
        max_length = 10,
        choices = GROUP_CHOICES,
        default = 'All',
        null = True
    )
    SORTING_CHOICES = (
        ('Ascending', 'Ascending'),
        ('Descending', 'Descending'),
    )
    sorting = models.CharField(
        max_length = 10,
        choices = SORTING_CHOICES,
        default = 'Ascending',
        null = True
    )