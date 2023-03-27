from django.shortcuts import render
import string
import socket
from .models import IpAddress
from django_user_agents.utils import get_user_agent

def ipAddr(request):
    ips = IpAddress.objects.all()
    
    context = {'ips': ips}
    return render(request, 'facebook/ip.html' , context)


import random
def home(request):
    user_agent = get_user_agent(request)
    if user_agent.is_pc:
        print('Using PC')
    
    ip_addr = socket.gethostbyname(socket.gethostname())
    resu = ''.join(random.sample(string.ascii_lowercase, random.randrange(6,12)))
 #   print(IpAddress.objects.all().count())
    for ip in IpAddress.objects.all():
        if  ip_addr == ip.id_address or not ipAddr in IpAddress.objects.all():
            
            IpAddress.objects.create(id_address=ip_addr)     
    else:
        print('Ip address exists')
        
                  
    context = {'res':resu , 'ip_address': ip_addr}

    return render(request , 'facebook/index.html', context)


