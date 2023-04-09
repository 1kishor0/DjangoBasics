from django.db import models

# Create your models here.
class Musician(models.Model):
    #id=models.AutoField("primary_key=True")
    firstName=models.CharField(max_length=30,blank=False)
    lastName=models.CharField(max_length=30)
    instrument=models.CharField(max_length=100)

    def __str__(self):
        return self.firstName+" "+self.lastName
    

class Album(models.Model):
   # id=models.AutoField("primary_key=True")
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    releaseDate=models.DateField()

    rating=(
        (1,"Worst"),
        (2,"Bad"),
        (3,"Not Bad"),
        (4,"Good"),
        (5,"Excellent"),
    )
    num_stars=models.IntegerField(choices=rating)


    def __str__(self):
        return self.name+", Rating: "+str(self.num_stars)
    