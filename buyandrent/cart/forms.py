from django import forms

HOUSE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddHouseForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                    choices = HOUSE_QUANTITY_CHOICES,
                                    coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
    