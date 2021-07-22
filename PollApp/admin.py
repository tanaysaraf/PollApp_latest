from django.contrib import admin
from .models import model_PollApp_Question,model_PollApp_Answers
# Register your models here.
admin.site.register(model_PollApp_Question)
admin.site.register(model_PollApp_Answers)

