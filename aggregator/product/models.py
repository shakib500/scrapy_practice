from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    img = models.CharField(max_length=200)

    # For converting the string into integer
    # find_number = [n for n in re.findall(r'(\d+)', string.replace(',', ''))]
