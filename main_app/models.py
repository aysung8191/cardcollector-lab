from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.
class Cover(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('covers_detail', kwargs={'pk': self.id})

class Card(models.Model):
    athlete = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    set = models.CharField(max_length=100)
    year_manufactured = models.IntegerField()
    features = models.TextField(max_length=250)
    covers = models.ManyToManyField(Cover)

    def __str__(self):
        return self.athlete
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})
    

class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']