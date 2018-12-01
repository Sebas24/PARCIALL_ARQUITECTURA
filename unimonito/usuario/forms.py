from django import forms

class loginForm(forms.Form):
    user_name=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'usuario', 'placeholder':'Usuario'}))
    password=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'password', 'placeholder':'Password'}))

class registroForm(forms.Form):
	empl_nombre=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'nombre', 'placeholder':'Nombre'}))
	empl_cedula=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'cedula', 'placeholder':'Cedula'}))
	empl_telefono=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'telefono', 'placeholder':'Telefono'}))
	empl_salario=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'salario', 'placeholder':'Salario'}))
	empl_pasword=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'password', 'placeholder':'Password'}))
