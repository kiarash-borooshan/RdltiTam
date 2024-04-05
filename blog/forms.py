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
                               widget=forms.RadioSelect,
                               label='جنسیت')
    address = forms.CharField(widget=forms.Textarea,
                              max_length=250,
                              label='آدرس')
    first_name = forms.CharField(max_length=30,
                                 label='نام ',
                                 help_text=" نام را وارد کنید ",
                                 required=False)
    last_name = forms.CharField(max_length=11,
                                label='نام خانوادگی')
    age = forms.IntegerField(label='سن')

    def clean_first_name(self):
        n = self.cleaned_data["first_name"]
        if len(n) < 5:
            return n
        else:
            raise forms.ValidationError("تعداد کاراکتر نام بیشتر از ۵ است")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError("شماره تلفن باید عددی باشد")
            else:
                return phone

    def clean_age(self):
        v = self.cleaned_data["age"]
        if v:
            if v < 0:
                return v
            else:
                return forms.ValidationError("تعداد ارقام سن نباید منفی باشد ")
