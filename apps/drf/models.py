from django.db import models

# Create your models here.
class Enterprise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    nit = models.IntegerField(blank= True, null = True)
    gln = models.IntegerField(blank=False, null = False)
    
    class Meta:
        verbose_name = "Enterprise"
        verbose_name_plural = "Enterprises"
    
    REQUIRED_FIELDS =['name', 'gln']    
    
    def __str__(self):
        return "{}".format(self.name)
    
    
class Code(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Enterprise, on_delete = models.CASCADE)
    name = models.CharField(max_length=150,blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    
    class Meta:
        verbose_name = "Code"
        verbose_name_plural = "Code"
        
    REQUIRED_FIELDS = ['name', 'owner']
    
    def __str__(self): 
        return "{}".format(self.name)
