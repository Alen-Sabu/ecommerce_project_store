from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField

class BillingAddressForm(forms.ModelForm):
   
    
    
    
    phone_number = PhoneNumberField(region="IN",max_length=15, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone-Number'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    country = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Country'}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Address'}))
    state = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'State'}))
    city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'City'}))
    district = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'District'}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control', "placeholder":"Pin-Code"}))
    status = forms.BooleanField(required = False,widget=forms.CheckboxInput(attrs={"class":"form-control", "id":"status-check","style":"width:15%;"}))
    
    
    class Meta:
        model = BillingAddress
        fields = [ 'phone_number', 'email', 'country','address', 'city','state', 'district','pincode', 'status']

class ShippingAddressForm(forms.ModelForm):
   
    
    
    
    phone_number = PhoneNumberField(region="IN",max_length=15, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone-Number'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    country = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Country'}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Address'}))
    state = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'State'}))
    city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'City'}))
    district = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'District'}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control', "placeholder":"Pin-Code"}))
    
    
    
    class Meta:
        model = ShippingAddress
        fields = [ 'phone_number', 'email', 'country','address', 'city','state', 'district','pincode']


class CouponForm(forms.Form):
    code = forms.CharField(required = False, widget=forms.TextInput(attrs={'id':'coupon-input',"class":"form-control coupon-input"}))
    
    class Meta:
        model = Coupon
        fields = ['code']

class ReturnForm(forms.Form):
    
    reason = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"class":"form-control"}))

    class Meta:
        model = Return
        fields = ['reason']
    # def __init__(self, user_id, order_id, *args, **kwargs):
    #     super(ReturnForm, self).__init__(*args, **kwargs)
    #     self.fields['item'].choices = self.get_ordered_items(user_id, order_id)

    # def get_ordered_items(self, user_id, order_id):
    #     items = []
    #     order = Orders.objects.get(customer =user_id, id=order_id)
    #     order_items = OrderedItems.objects.filter(order = order)
    #     for item in order_items:
    #         items.append((item.id, str(item)))
    #     return items