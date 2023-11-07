from django import forms

class JobApplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)

    employment_choices = (
        ('None', '--Please Choose--'),
        ('ft', 'full-time'),
        ('pt', 'part-time'),
    )
    employment_type = forms.ChoiceField(choices=employment_choices)

    start_date = forms.DateField(
        help_text='The earliest date you can start working'
    )

    day_choices = (
        ('1', 'MON'),
        ('2', 'TUE'),
        ('3', 'WED'),
        ('4', 'THU'),
        ('5', 'FRI'),
        ('6', 'SAT'),
        ('7', 'SUN'),
    )
    available_days = forms.MultipleChoiceField(
        choices=day_choices,
        help_text='Select all days that you can work.'
    )

    desired_hourly_wage = forms.DecimalField(decimal_places=2)
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(
        label="I certify that the information I have provided is true."
    )
