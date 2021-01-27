from django.contrib import admin
from .models import Question,choice

# Register your models here.
# Đăng ký models lên admin
admin.site.register(Question)
admin.site.register(choice)
