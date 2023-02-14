from django import forms

class HostelAppForm(forms.Form):
    CHOICES = (
        (2, '2 bed'),
        (4, '4 bed'),
        (8, '8 bed')
    )
    profile_id = forms.IntegerField(widget=forms.HiddenInput)
    bed_spaces = forms.ChoiceField(choices=CHOICES, required=False)
