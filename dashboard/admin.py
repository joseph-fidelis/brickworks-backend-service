from django.contrib import admin
from .models import IngestionLog, TaskHistory,UploadedXML,Category,Color,Gear,Minifigure,Part,PartWithColor
# Register your models here.
admin.site.register(TaskHistory)
admin.site.register(IngestionLog)
admin.site.register(UploadedXML)
admin.site.register(Color)
admin.site.register(Gear)
admin.site.register(Category)
admin.site.register(Minifigure)
admin.site.register(Part)
admin.site.register(PartWithColor)