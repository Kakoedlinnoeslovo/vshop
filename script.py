# -*- coding: utf-8 -*-
import os
import sys
import csv
import random

#cкрипт, который создает новые продукты, используя product.csv

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vshop.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


from vshop_app.models import Item

k=10

item_list=[]
with open('products.csv', "rt") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(spamreader):
        if i!=0 and i<k:
            for j,word in enumerate(row):
                if j!=0:
                    if word.isdigit() !=True:
                        title = word
                        item_list.append(Item(title=title))
Item.objects.bulk_create(item_list)

