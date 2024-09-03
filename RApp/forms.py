from .models import User,seProfile,byProfile,Property
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms


class AusForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","eid","role_type_appl","role_type"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2", 
			"placeholder":"Username",
			}),
		"role_type_appl":forms.Select(attrs={
			"class":"form-control my-2",
			}),
        "mble":forms.TextInput(attrs={
            "class":"form-control my-2",
			"placeholder":"Enter Mobile no",
            }),
        "gdr":forms.Select(attrs={
			"class":"form-control my-2",
            }),
	    "role_type":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UsuserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","role_type_appl","email","mble","gdr"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-3",
			"placeholder":"Username",
			}),
		"role_type_appl":forms.Select(attrs={
			"class":"form-control my-3",
			}),
        "email":forms.TextInput(attrs={
            "class":"form-control my-3",
			"placeholder":"Enter Mail",
            }),
		"mble":forms.TextInput(attrs={
            "class":"form-control my-3",
			"placeholder":"Enter Mobile no",
            }),		
        "gdr":forms.Select(attrs={
			"class":"form-control my-3",
            }),
		}
class UslistForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","email","role_type"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-3",
			"placeholder":"Username",
			}),
		"role_type":forms.Select(attrs={
			"class":"form-control my-3",
			}),
		"email":forms.TextInput(attrs={
            "class":"form-control my-3",
			"placeholder":"Enter Mail",
            }),
		}
class UpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
    class Meta:
        model = User
        fields = ["username","eid","email","mble","role_type"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Username",
                    }),
            "eid":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":"true",
                }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Email",
                }),
            "mble":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Mobile No",
                }),
            "role_type":forms.Select(attrs={
                "class":"form-control my-2",
            }),
        }
class UdForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","eid","email","mble","role_type"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Username",
                    }),
            "eid":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":"true",
                }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Email",
                }),
            "mble":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Mobile No",
                }),
            "role_type":forms.Select(attrs={
                "class":"form-control my-2",
            }),
        }
class chgPwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"old Password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"New Password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model=User
		fields="__all__"
class UspForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","mble","gdr","pfimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mailid",
			}),
		"mble":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		"gdr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"pfimg":forms.ClearableFileInput(attrs={
				"class":"form-control-file my-2",
			}),
		}

class SellForm(forms.ModelForm):
	class Meta:
		model = seProfile
		fields = ["sellang","selage","seloc","selltypes","sellinfo","sellexpr","sellcerti",]
		widgets = {
		"sellang":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Language",
			}),
		"selage":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Age",
			}),
		"seloc":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Location",
			}),
		"selltypes":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"sellinfo":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			}),
		"sellexpr":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Experience",
			}),
		"sellcerti":forms.ClearableFileInput(attrs={
				"class":"form-control-file my-2",
			}),
		}


class BuyForm(forms.ModelForm):
	class Meta:
		model=byProfile
		fields=["buylang","buyage","buyloc","buytypes","buyinfo",]
		widgets ={
			"buylang":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Language",
			}),
			"buyage":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Age",
			}),
			"buylang":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Language",
			}),
			"buyloc":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Location",
			}),
			"buytypes":forms.Select(attrs={
				"class":"form-control my-2",
			}),
			"buyinfo":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Address",
			}),
		}

class PropForm(forms.ModelForm):
	class Meta:
		model = Property
		fields=["proptitle","proptype","propcity","propstate","propzipcode","propsqft","propprice","propdesc","main_photo","photo_1","photo_2","propdoc",]
		widgets ={
			"proptitle":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter title",
			}),
			"proptype":forms.Select(attrs={
				"class":"form-control my-2",
			}),
			"propcity":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter City",
			}),
			"propstate":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter State",
			}),
			"propzipcode":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Zipcode",
			}),
			"propsqft":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter property size in Sqft",
			}),
			"propprice":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter price",
			}),
			"main_photo":forms.ClearableFileInput(attrs={
				"class":"form-control-file my-2",
			}),
			"photo_1":forms.ClearableFileInput(attrs={
				"class":"form-control-file my-2",
			}),
			"photo_2":forms.ClearableFileInput(attrs={
				"class":"form-control-file my-2",
			}),
			"propdesc":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Description",
			}),
			"propdoc":forms.ClearableFileInput(attrs={
				"class":"form-control-file my-2",
			}),
		}

class PropdelForm(forms.ModelForm):
	class Meta:
		model = Property
		fields=["propown","proptitle","proptype","propcity","propzipcode","propsqft","propprice",]
		widgets ={
			"propown":forms.TextInput(attrs={
				"class":"form-control my-2",
				"readonly":"true",
			}),
			"proptitle":forms.TextInput(attrs={
				"class":"form-control my-2",
				"readonly":"true",

			}),
			"proptype":forms.Select(attrs={
				"class":"form-control my-2",
				"readonly":"true",
			}),
			"propcity":forms.TextInput(attrs={
				"class":"form-control my-2",
				"readonly":"true",
			}),
			"propzipcode":forms.TextInput(attrs={
				"class":"form-control my-2",
				"readonly":"true",
			}),
			"propsqft":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"readonly":"true",
			}),
			"propprice":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"readonly":"true",
			}),
		}

class PropsellForm(forms.ModelForm):
	class Meta:
		model = Property
		fields=["propstatus","propsoldto",]
		widgets ={
			"propstatus":forms.Select(attrs={
				"class":"form-control my-2",
			}),
			"propsoldto":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Enter Id of buyer",
			}),
		}

class ApproveForm(forms.ModelForm):
	class Meta:
		model = User
		fields=["eid","username","email","role_type",]
		widgets = {
			"eid":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":"true",
                }),
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
				"readonly":"true"
                }),
			"email":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":"true",
                }),
			"role_type":forms.Select(attrs={
                "class":"form-control my-2",
            }),
			
		}

class Buymailtosell(forms.ModelForm):
	class Meta:
		model = User 
		fields=["eid","username","email",]
		widgets = {
			"eid":forms.TextInput(attrs={
                "class":"form-control my-2",   
                "readonly":"true",
                }),
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
				"readonly":"true"
                }),
			"email":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":"true",
                }),
		}
 

