from django import forms
from models import Link


class AddLinkForm(forms.Form):
	name = forms.CharField(max_length=500)
	href=forms.URLField()
	
	def save(self):
		new_link=Link(**self.cleaned_data)
		new_link.status='submitted'
		new_link.put()
		



