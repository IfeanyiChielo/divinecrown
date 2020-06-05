# from django import forms
# from .models import Postrec
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model= Postrec
#         fields = '__all__'
#     #fields= ['title','content']

from .models import Soapprod, Staffrec, Creamprod, Soapsales, Creamsales
from django.forms import ModelForm
class StaffrecForm(ModelForm):
   class Meta:
    model = Staffrec
    fields = '__all__'


from django import forms
from pages.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta:
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

# try crud

# from django import forms
from .models import Staffrec, Staffinfo

# class EmployeeForm(forms.ModelForm):

#     class Meta:
#         model = Employee
#         fields = ('fullname','mobile','emp_code','position')
#         labels = {
#             'fullname':'Full Name',
#             'emp_code':'EMP. Code'
#         }

#     def __init__(self, *args, **kwargs):
#         super(EmployeeForm,self).__init__(*args, **kwargs)
#         self.fields['position'].empty_label = "Select"
#         self.fields['emp_code'].required = False

    # forms soap production 
class SoapprodForm(forms.ModelForm):
    class Meta:
        model = Soapprod
        fields ='__all__'
        labels = {
            'Serial_White_Guava':'Serial_White_Guava',
            'Serial_White_Premium':'Serial_White_Premium'
        }

class StaffrecForm(forms.ModelForm):

    class Meta:
        model = Staffrec
        fields = '__all__'
        labels = {
            
            'fullname':'Full Name',
            'address':'Address'
        }
class CreamprodForm(forms.ModelForm):
    class Meta:
        model = Creamprod
        fields ='__all__'

class StaffinfoForm (forms.ModelForm):
     class Meta:
        model = Staffinfo
        fields ='__all__'

class SoapsalesForm(forms.ModelForm):
    class Meta:
        model = Soapsales
        fields ='__all__'

class CreamsalesForm(forms.ModelForm):
    class Meta:
        model = Creamsales
        fields ='__all__'