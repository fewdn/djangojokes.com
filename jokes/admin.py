from django.contrib import admin

from .models import Category, Joke, JokeVote, Tag
from common.admin import DjangoJokesAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(DjangoJokesAdmin):  #use custom admin instead of admin.ModelAdmin
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return()
    

@admin.register(Joke)
class JokeAdmin(DjangoJokesAdmin): #use custom admin instead of admin.ModelAdmin
    model = Joke
    # list_display is not required but without it all rows have a single column (string value of model class)
    # Using it, sets column headings in Django's web admin interface
    date_hierarchy = 'updated'
    list_display = ['question', 'created', 'updated']  # fields that will show in Django admin, rows of jokes   
    list_filter = ['updated', 'category', 'tags']
    ordering = ['-updated']
    search_fields = ['question', 'answer']  # search box text will search these fields for a match

    # readonly_fields holds field that you can read but NOT EDIT
    # An alternative syntax is using that attribute readonly_fields = ('created', 'updated')
    # but the fields will show up BLANK in the form when adding new jokes (created and updated not created until inserted)  
    # There is no need to display blank read only fields, so its best not to use the readonly_fields attribute.
    # Using the getter function checks to see if the object exists
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')   # If editing created,updated is returned
        
        return ()  # If creating a new joke an empty tuple is returned, indicating there are no readonly fields
    
@admin.register(JokeVote)
class JokeVoteAdmin(DjangoJokesAdmin): #use custom admin instead of admin.ModelAdmin 
    model = JokeVote
    list_display = ['joke', 'user', 'vote']

    def get_readonly_fields(self, request, obj=None):
        if obj: #editing an existing object
            return ('created', 'updated')
        return()

@admin.register(Tag)
class TagAdmin(DjangoJokesAdmin): #use custom admin instead of admin.ModelAdmin
    model = Tag
    list_display = ['tag', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return()
