# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Test(models.Model):
    homeplanet = models.FloatField(db_column='HomePlanet', blank=True, null=True)  # Field name made lowercase.
    cryosleep = models.FloatField(db_column='CryoSleep', blank=True, null=True)  # Field name made lowercase.
    destination = models.FloatField(db_column='Destination', blank=True, null=True)  # Field name made lowercase.
    age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    roomservice = models.FloatField(db_column='RoomService', blank=True, null=True)  # Field name made lowercase.
    foodcourt = models.FloatField(db_column='FoodCourt', blank=True, null=True)  # Field name made lowercase.
    shoppingmall = models.FloatField(db_column='ShoppingMall', blank=True, null=True)  # Field name made lowercase.
    spa = models.FloatField(db_column='Spa', blank=True, null=True)  # Field name made lowercase.
    vrdeck = models.FloatField(db_column='VRDeck', blank=True, null=True)  # Field name made lowercase.
    transported = models.IntegerField(db_column='Transported', blank=True, null=True)  # Field name made lowercase.
    cabin_deck = models.FloatField(db_column='Cabin_Deck', blank=True, null=True)  # Field name made lowercase.
    cabin_num = models.IntegerField(db_column='Cabin_Num', blank=True, null=True)  # Field name made lowercase.
    cabin_side = models.FloatField(db_column='Cabin_Side', blank=True, null=True)  # Field name made lowercase.
    passengerid = models.CharField(db_column='PassengerId', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'


class Train(models.Model):
    homeplanet = models.FloatField(db_column='HomePlanet', blank=True, null=True)  # Field name made lowercase.
    cryosleep = models.FloatField(db_column='CryoSleep', blank=True, null=True)  # Field name made lowercase.
    destination = models.FloatField(db_column='Destination', blank=True, null=True)  # Field name made lowercase.
    age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    roomservice = models.FloatField(db_column='RoomService', blank=True, null=True)  # Field name made lowercase.
    foodcourt = models.FloatField(db_column='FoodCourt', blank=True, null=True)  # Field name made lowercase.
    shoppingmall = models.FloatField(db_column='ShoppingMall', blank=True, null=True)  # Field name made lowercase.
    spa = models.FloatField(db_column='Spa', blank=True, null=True)  # Field name made lowercase.
    vrdeck = models.FloatField(db_column='VRDeck', blank=True, null=True)  # Field name made lowercase.
    transported = models.IntegerField(db_column='Transported', blank=True, null=True)  # Field name made lowercase.
    cabin_deck = models.FloatField(db_column='Cabin_Deck', blank=True, null=True)  # Field name made lowercase.
    cabin_num = models.IntegerField(db_column='Cabin_Num', blank=True, null=True)  # Field name made lowercase.
    cabin_side = models.FloatField(db_column='Cabin_Side', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'train'
