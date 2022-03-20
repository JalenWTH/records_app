from django.db import models

class record_jalen(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField(default=0)
    occupation=models.CharField(max_length=20)

    def __str__(self):
            return f'{self.first_name} {self.last_name} {self.age} {self.occupation}'

class record_teah(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField(default=0)
    occupation=models.CharField(max_length=20)

    def __str__(self):
            return f'{self.first_name} {self.last_name} {self.age} {self.occupation}'

class record_sheila(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField(default=0)
    occupation=models.CharField(max_length=20)

    def __str__(self):
            return f'{self.first_name} {self.last_name} {self.age} {self.occupation}'

class record_marie(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField(default=0)
    occupation=models.CharField(max_length=20)

    def __str__(self):
            return f'{self.first_name} {self.last_name} {self.age} {self.occupation}'

class record_deion(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField(default=0)
    occupation=models.CharField(max_length=20)

    def __str__(self):
            return f'{self.first_name} {self.last_name} {self.age} {self.occupation}'

records = []

records.append(record_jalen)
records.append(record_teah)
records.append(record_sheila)
records.append(record_marie)
records.append(record_deion)