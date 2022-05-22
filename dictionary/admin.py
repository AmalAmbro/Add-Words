from django.contrib import admin

from dictionary.models import WordMeaning, Words



class WordMeaningAdmin(admin.ModelAdmin):
    list_display = ["id","word",'meaning','priority']
admin.site.register(WordMeaning, WordMeaningAdmin)

class WordAdmin(admin.ModelAdmin):
    list_display = ["id","word"]
    
admin.site.register(Words, WordAdmin)
