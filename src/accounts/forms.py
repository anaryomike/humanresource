from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserAddForm(UserCreationForm):
	'''
	Extending UserCreationForm - with email

	'''
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg.edwards@rabotecgroup.com'}))

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		

	def clean_email(self):
		email = self.cleaned_data['email']
		qry = User.objects.filter(email = email)

		domain_list = ['rabotecgroup.com','rabotecghana.com']
		get_rabotec_domain = email.split('@')[1]#get me whatever after @, eg. gmail.com

		print(get_rabotec_domain in domain_list)

		if qry.exists():
			'''
			True - Queryset exist run validation message here
			'''
			raise forms.ValidationError('email {0} already exists'.format(email))


		elif get_rabotec_domain not in domain_list:
			print('test - not in domain')
			raise forms.ValidationError('email does not contain domain')

		return email






class UserLogin(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))


