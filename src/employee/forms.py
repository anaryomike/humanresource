from django import forms
from employee.models import Role,Department,Nationality,Religion,Bank,Emergency,Relationship,Employee
from django.contrib.auth.models import User


# EMPLoYEE
class EmployeeCreateForm(forms.ModelForm):
	employeeid = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'please enter 5 characters without RGL or slashes eg. A0025'}))
	image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'previewImage(this);'}))
	class Meta:
		model = Employee
		exclude = ['is_blocked','is_deleted','created','updated']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}


	# def clean_user(self):
	# 	user = self.cleaned_data['user'] #returns <User object>,not id as in [views <-> templates]

	# 	qry = Employee.objects.filter(user = user)#check, whether any employee exist with username - avoid duplicate users - > many employees
	# 	if qry:
	# 		raise forms.ValidationError('Employee exists with username already')
	# 	return user





class EmergencyCreateForm(forms.ModelForm):

	class Meta:
		model = Emergency
		fields = ['employee','fullname','tel','location','relationship']





# FAMILY

class FamilyCreateForm(forms.ModelForm):

	class Meta:
		model = Relationship
		fields = ['employee','status','spouse','occupation','tel','children','nextofkin','contact','relationship','father','foccupation','mother','moccupation']



class BankAccountCreation(forms.ModelForm):

	class Meta:
		model = Bank
		fields = ['employee','name','branch','account','salary']
