from django import forms
from apps.users.models import CustomUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class StudentRegisterForm(UserRegisterForm):
    class Meta(UserRegisterForm.Meta):
        fields = ['first_name', 'last_name','father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'student_group', 'address', 'gender', 'image', 'bio', 'zip_code']


class TeacherRegisterForm(UserRegisterForm):
    class Meta(UserRegisterForm.Meta):
        fields = ['first_name', 'last_name','father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'subject', 'address', 'gender', 'salary', 'image', 'bio', 'zip_code']
        

class ParentRegisterForm(UserRegisterForm):
    class Meta(UserRegisterForm.Meta):
        fields = ['first_name', 'last_name','father_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'children', 'address', 'gender', 'image', 'bio', 'zip_code']
        
        
class AdminRegisterForm(UserRegisterForm):
    class Meta(UserRegisterForm.Meta):
        fields = ['first_name', 'last_name','father_name', 'date_of_birth', 'email', 'phone_number', 'password',
                  'address', 'gender', 'image', 'bio', 'zip_code']