from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message = f'{value} is in the past.', code='past_date'
        )


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
    )

    # Default widget for CharField is TextInput
    first_name = forms.CharField(
        # for single-named attributes use True. 'autofocus': True vs 'autofocus':'autofocus'
        widget=forms.TextInput(attrs={'autofocus':True})  
    )
    last_name = forms.CharField()
    email = forms.EmailField()

    # Default widget for URLField is URLInput
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder':'https://wwww.example.com', 'size': '50'}
        ),
        validators=[URLValidator(schemes=['http', 'https'])]
    )

    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPES)

    start_date = forms.DateField(
        help_text='The earliest date you can start working',
        widget=forms.SelectDateWidget(
            years=YEARS,
            attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%;'}
        ),
        validators=[validate_future_date],
        error_messages={'past_date': 'Please enter a future date.'}
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
