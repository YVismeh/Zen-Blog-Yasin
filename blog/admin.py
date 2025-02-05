from django.contrib import admin
from .models import Agent, Category, Comments, Blog, SpecialService, Tag

# Register your models here.

admin.site.register(Agent)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Blog)
admin.site.register(SpecialService)
admin.site.register(Tag)