from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Category"

    name = models.CharField(max_length=500,verbose_name='Category')
    
    def __str__(self):
           return self.name

class Course(models.Model):
    class Meta:
        verbose_name_plural = "Courses"
        db_table = "Course"

    title = models.CharField(max_length=500,verbose_name='Title')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category')
    
    def __str__(self):
           return self.title