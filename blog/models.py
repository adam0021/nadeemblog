from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse



class Post(models.Model):
    title=models.CharField(max_length=120)
    image=models.ImageField(null=True,blank=True,width_field="width_field",height_field="height_field")
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    content=models.TextField()
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail",kwargs={"id":self.id})
        #return "/post/%s" %(self.id)
    

class comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments')
    text=models.TextField()
    created_date=models.DateTimeField(auto_now=False,auto_now_add=True)
    approved_comment=models.BooleanField(default=False)
