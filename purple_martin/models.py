# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Confirmed(models.Model):
    c_id = models.IntegerField(primary_key=True)
    ou = models.ForeignKey('Roosts', blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    month = models.CharField(max_length=24, blank=True)
    date = models.DateField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    observer = models.TextField(blank=True)
    institution = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'confirmed'


class Image(models.Model):
    im_id = models.IntegerField(primary_key=True)
    ou = models.ForeignKey('Roosts', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    image = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'image'


class LuSource(models.Model):
    code = models.IntegerField(primary_key=True)
    cource = models.CharField(max_length=55, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'lu_source'
    def __unicode__(self):
        return u'%d %s' % (self.code, self.cource)

class RadarObs(models.Model):
    ro_id = models.IntegerField(primary_key=True)
    ou = models.ForeignKey('Roosts', blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    ref_date = models.DateField(blank=True, null=True)
    ref_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radar_obs'


class Roosts(models.Model):

    ou_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    soar_no = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    source = models.ForeignKey(LuSource, db_column='source', blank=True, null=True)
    nex2004 = models.SmallIntegerField(blank=True, null=True)
    loc_source_comment = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'roosts'


class Wsr(models.Model):
    st_id = models.IntegerField(primary_key=True)
    station = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True)
    city = models.CharField(max_length=35, blank=True)

    class Meta:
        managed = False
        db_table = 'wsr'
