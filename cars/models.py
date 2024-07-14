from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rental_rate = models.DecimalField(max_digits=6, decimal_places=2)
    car_class = models.CharField(max_length=50)
    basic_features = models.JSONField()
    additional_features = models.JSONField()
    year_of_manufacturing = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='car_images/')
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.name}"
