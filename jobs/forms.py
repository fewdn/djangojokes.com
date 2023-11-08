from datetime import datetime
from django import forms

# REFERENCE: https://docs.djangoproject.com/en/4.2/ref/forms/fields/
class JobApplicationForm(forms.Form):
    date = datetime.now()
    year = date.year
    next_year = year + 1
    YEARS = [year, next_year]
    EMPLOYMENT_TYPES = (
        ('None', '--Please Choose--'),
        ('ft', 'full-time'),
        ('pt', 'part-time'),
    )
    DAYS = (
        ('1', 'MON'),
        ('2', 'TUE'),
        ('3', 'WED'),
        ('4', 'THU'),
        ('5', 'FRI'),
        ('6', 'SAT'),
        ('7', 'SUN'),
    )

    # Default widget for CharField is TextInput
    first_name = forms.CharField(
        # for single-named attributes use True. 'autofocus': True vs 'autofocus':'autofocus'
        widget=forms.TextInput(attrs={'autofocus':True})  
    )
    last_name = forms.CharField()
    email = forms.EmailField()

    # Default widget for URLField is URLInput
    website = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={'placeholder':'https://wwww.example.com', 'size': '50'}
        )
    )

    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPES)

    start_date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=YEARS,
        ),
        help_text='The earliest date you can start working'
    )

    # For single value attributes use 'checked':True, instead of "checked":"checked"
    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text='Check all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked': True}  
        )
    )

    # Default widget for DecimalField is NumberInput
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'min': '10.00', 'max': '100.00', 'step': '.25'}
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea( attrs={'cols': '75', 'rows': '5'})
    )
    confirmation = forms.BooleanField(
        label="I certify that the information I have provided is true."
    )
