from django.db import models

# Create your models here.

#############################################
#               Scraping tables             #
#############################################
class History(models.Model):
    date_observed = models.DateField()
    time_observed = models.TimeField()
    sport = models.TextField()
    match = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    odds1 = models.FloatField()
    oddsx = models.FloatField()
    odds2 = models.FloatField()
    margin = models.FloatField()
    bookie1 = models.TextField()
    bookiex = models.TextField()
    bookie2 = models.TextField()
    class Meta:
        managed = True
        db_table = 'history'


class Arbs(models.Model):
    sport = models.TextField()
    match = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    odds1 = models.FloatField()
    oddsx = models.FloatField()
    odds2 = models.FloatField()
    margin = models.FloatField()
    bookie1 = models.TextField()
    bookiex = models.TextField()
    bookie2 = models.TextField()
    class Meta:
        managed = True
        db_table = 'arbs'
        constraints = [models.UniqueConstraint(fields = ['date','match'], name='date_match')]

class Scrape(models.Model):
    bookie = models.TextField()
    bet_id = models.IntegerField(unique = True)
    event_date = models.DateField()
    event_time = models.TimeField()
    sport = models.TextField()
    competition = models.TextField()
    match = models.TextField()
    odds1 = models.FloatField()
    oddsx = models.FloatField()
    odds2 = models.FloatField()
    class Meta:
        managed = True
        db_table = 'scrape'