from django.contrib import admin

from .models import Joke

# Register your models here.
@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke
    # list_display is not required but without it all rows have a single column (string value of model class)
    # Using it, sets column headings in Django's web admin interface
    list_display = ['question', 'created', 'updated']  # fields that will show in Django admin, rows of jokes

    # readonly_fields holds field that you can read but NOT EDIT
    # An alternative syntax is using that attribute readonly_fields = ('created', 'updated')
    # but the fields will show up BLANK in the form when adding new jokes (created and updated not created until inserted)  
    # There is no need to display blank read only fields, so its best not to use the readonly_fields attribute.
    # Using the getter function checks to see if the object exists
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated')   # If editing created,updated is returned
        
        return ()  # If creating a new joke an empty tuple is returned, indicating there are no readonly fields