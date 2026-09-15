from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=15, blank=True, null=True) # phone -> mobile nu maathiten
    phone = models.CharField(max_length=15, blank=True, null=True) # pazhaya phone iruntha blank aakiten
    village = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='complaints/', blank=True, null=True)
    petition_photo = models.ImageField(upload_to='petitions/', blank=True, null=True)
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Processing', 'Processing'),
            ('Resolved', 'Resolved'),
        ],
        default='Pending'
    )

    def __str__(self):
        return self.name