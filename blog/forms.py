from .models import Account
from django import forms


# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = ("gender", "address")


class AccountForm(forms.Form):
    GENDER_CHOICES = (
        ("آقا", "آقا"),
        ("خانم", "خانم")
    )
    phone = forms.CharField(max_length=11, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               required=True,
                               widget=forms.RadioSelect)
    address = forms.CharField(widget=forms.Textarea,
                              max_length=250)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
