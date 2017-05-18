# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):      #table that inherits from Model from models
	title = models.CharField(max_length=140) #column name and data type
	body = models.TextField() 
	date = models.DateTimeField()

	def __unicode__(self):
		return self.title
	
