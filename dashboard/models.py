from django.db import models
from django.utils import timezone

class TaskHistory(models.Model):
    task_id = models.CharField(max_length=255, unique=True)
    script_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="PENDING")
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.duration = self.end_time - self.start_time
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.script_name} ({self.task_id}) - {self.status}"



class IngestionLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.created_at}] {self.message[:50]}"


class UploadedXML(models.Model):
    file = models.FileField(upload_to="data/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
class Category(models.Model):
    id = models.CharField( max_length=255)
    category_id = models.CharField(primary_key=True, max_length=255)
    category_name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'category'  
        ordering = ['category_name']
        indexes = [ models.Index(fields=['category_name'], name='idx_category_name') ]

class Color(models.Model):
    
    color_id = models.CharField(primary_key=True, max_length=255)
    color_name = models.CharField(max_length=255)
    color_type = models.CharField(max_length=255)
    color_code = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'color'  
        ordering = ['color_name']
        indexes = [
            models.Index(fields=['color_name'], name='idx_color_name'),
            models.Index(fields=['color_type'], name='idx_color_type'),
            models.Index(fields=['color_type', 'color_name'], name='idx_color_type_name'),
        ]


class Part(models.Model):
    
    item_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    
    class Meta:
        db_table = 'parts'  
        ordering = ['name']
        indexes = [ models.Index(fields=['name'], name='idx_part_name') ]


class Gear(models.Model):
    
    item_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    
    class Meta:
        db_table = 'gears'  
        ordering = ['name']
        indexes = [ models.Index(fields=['name'], name='idx_gear_name') ]
        
class Minifigure(models.Model):
    
    item_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    
    class Meta:
        db_table = 'minifigures'  
        ordering = ['name']
        indexes = [ models.Index(fields=['name'], name='idx_minifigure_name') ]
        
class PartWithColor(models.Model):
    
    sn = models.CharField(primary_key=True, max_length=255)
    item_id = models.CharField(max_length=255)
    color_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    
    
    class Meta:
        db_table = 'parts_with_colors'  
        ordering = ['item_id']
        indexes = [ models.Index(fields=['item_id'], name='idx_parts_with_color_id') ]