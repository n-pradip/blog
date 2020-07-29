from django import forms

class contacts_form(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'id':"name","aria-describedby":"name"}))
    phone_no = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type':"phone",'class':"form-control",'id':"phone"}))
    email = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type':"email",'class':"form-control",'id':"email","aria-describedby":"emailHelp"}))
    contact_issue = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", "aria-describedby":"name"}))
    #time = forms.DateTimeField(auto_now_add=True, blank=True)
