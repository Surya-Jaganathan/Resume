from django.db import models


class edu(models.Model):
    name = models.TextField()
    board = models.CharField(max_length=100)
    yop = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)
    degree = models.CharField(max_length=150)

    class Meta:
        db_table = "education"


class intern(models.Model):
    com = models.CharField(max_length=150)
    period = models.CharField(max_length=150)
    inn = models.TextField()

    class Meta:
        db_table = "intern"


class skill(models.Model):
    ski = models.TextField()

    class Meta:
        db_table = "skill"


class home(models.Model):
    heading = models.TextField()
    content = models.TextField()

    class Meta:
        db_table = "home_content"


class query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    qu = models.TextField()
    time = models.TextField()

    class Meta:
        db_table = "Customer Query"
