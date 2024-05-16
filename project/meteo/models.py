from django.db import models

# Create your models here.


class React(models.Model):
    Lieu= models.CharField(max_length=100)
    Date = models.DateField(auto_now_add=True)
    temp= models.CharField(max_length=10)
    vent=models.CharField(max_length=10)
    precepitation= models.CharField(max_length=10)
    humidite= models.CharField(max_length=10)
    

    def __str__(self):
        return f"{self.Lieu} - {self.Date} - {self.temp}-  {self.vent} - {self.precepitation} - {self.humidite}"
    

class Wilaya(models.Model):

        id_wilaya=models.IntegerField(primary_key=True)
        wilaya_nom = models.CharField(max_length=100)
        

        def __str__(self):
            return self.wilaya_nom
        

class ConditionMeteoWilayas(models.Model):
    y=[
        ('pluvieux','pluie'),
        ('ensoleille','ensoleille'),
        ('nuageux','nuageux'),
    
        ]
    temp = models.IntegerField()
    vent = models.DecimalField(max_digits=2,decimal_places =2)
    precepitation  = models.IntegerField()
    humidite = models.IntegerField()
    icon = models.CharField(choices=y,default='ensoleille')
    wilaya_id = models.ForeignKey(Wilaya,on_delete=models.PROTECT,null=True,blank=True)







