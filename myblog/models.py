from django.db import models





class IpAddress(models.Model):
    id_address = models.CharField(max_length=20)
    
    
    
    def __str__(self):
        
        return f'the Ip address: {self.id_address}'
