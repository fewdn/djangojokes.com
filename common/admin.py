from django.contrib import admin

# Register your models here.

admin.site.index_title = 'Home'
admin.site.site_title = 'Django Jokes Admin'
admin.site.site_header = 'Django Jokes Admin'

# A custom ModelAdmin to import to your other models
# allowing you to specify number of objects per page, etc.
class DjangoJokesAdmin(admin.ModelAdmin):
    list_per_page=25
    list_max_show_all = 1000
    save_as = True # "save as new" button replaces "save and add another"
                   # To change this in a Form View modify "save_as" in the inheriting class
