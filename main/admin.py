from django.contrib import admin
from . models import plants
from . models import predict
from . models import news

# Register your models here.
admin.site.register(plants)
admin.site.register(predict)
admin.site.register(news)