from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, Http404        
from vshop_app.models import Item
from vshop_app.models import User
import random
# Create your views here.:
def user_page(request):
   try:
      items = Item.objects.all()
      user=random.choice(User.objects.all())
   except:
      raise Http404('Requested user not found.')
   template = get_template('home.html')
   variables = dict()
   variables['user']  = user
   variables['items'] = items
   output = template.render(variables)
   return HttpResponse(output)
