from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, Http404

from vshop_app.models import Item
from vshop_app.models import User

from vshop_app.forms import EditTextForm

import random
import datetime
# Create your views here.:

def user_page(request):
   try:
      items = Item.objects.all()
      user=random.choice(User.objects.all())
   except:
      raise Http404('Requested item not found.')
   template = get_template('home.html')
   variables = dict()
   variables['user']  = user
   variables['items'] = items
   output = template.render(variables)
   return HttpResponse(output)



def item_about(request, item_id):
   if request.method == 'POST':
      form = EditTextForm(request.POST)
      if form.is_valid():
        try:
           item = Item.objects.get(id = item_id)
           item.text=form['text_field'].value()
           item.save()
        except:
           raise Http404('Requested item not found.1')
        now = datetime.datetime.now()
        html = "<html><body>Thank you, today is a good day and now is %s.</body></html>" % now
        return HttpResponse(html)
   else:
      variables = dict()
      try:
         item = Item.objects.get(id = item_id)
      except:
         raise Http404('Requested item not found.2')
      variables['item']  = item
      form = EditTextForm()
      variables['form']  = form
      template = get_template('edit.html')
      output = template.render(variables)
      return HttpResponse(output)

# def form_item(request):
#    if request.method == 'POST':
#       form = EditTextForm(request.POST)
#       if form.is_valid():
#          now = datetime.datetime.now()
#          html = "<html><body>Thank you, today is a good day and now is %s.</body></html>" % now
#          return HttpResponse(html)
#       else:
#          form = EditTextForm()
#          return render_to_response('edit.html', {‘form’: form})


