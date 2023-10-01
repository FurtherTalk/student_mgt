import re
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 
            'email', 'qq', 'phone',
        )

    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字! ')
        
        return int(cleaned_data)

    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字! ')
        
        return int(cleaned_data)
    
    # def clean_email(self):
    #     cleaned_data = self.cleaned_data['email']
    #     email_patt = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     if not re.match(email_patt, cleaned_data):
    #         raise forms.ValidationError('邮箱地址无效! ')
        
    #     return cleaned_data
    
    