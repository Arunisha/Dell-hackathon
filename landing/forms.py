from django import forms


class CommentForm(forms.Form):
	text = forms.CharField(max_length=200)


class CheckoutForm(forms.Form):
	Address = forms.CharField(widget=forms.Textarea)
	card_number = forms.IntegerField()
	card_cvv = forms.IntegerField()

