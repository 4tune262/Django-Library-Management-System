from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nhập tên"
        })
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nhập họ"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "example@gmail.com"
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Tên đăng nhập"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Mật khẩu"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Nhập lại mật khẩu"
        })
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#
#         exclude = ("user",)
#
#         widgets = {
#             "student_id": forms.TextInput(attrs={"class": "form-control"}),
#             "faculty": forms.TextInput(attrs={"class": "form-control"}),
#             "class_name": forms.TextInput(attrs={"class": "form-control"}),
#             "phone": forms.TextInput(attrs={"class": "form-control"}),
#             "address": forms.Textarea(attrs={
#                 "class": "form-control",
#                 "rows": 3
#             }),
#             "gender": forms.Select(attrs={"class": "form-select"}),
#             "birthday": forms.DateInput(attrs={
#                 "class": "form-control",
#                 "type": "date"
#             }),
#             "avatar": forms.FileInput(attrs={"class": "form-control"}),
#         }
class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        exclude = ("user",)

        widgets = {

            "student_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Mã sinh viên"
            }),

            "faculty": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Khoa"
            }),

            "class_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Lớp"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Số điện thoại"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Địa chỉ"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "birthday": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "avatar": forms.FileInput(attrs={
                "class": "form-control"
            }),
        }