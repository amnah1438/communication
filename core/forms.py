from django import forms
from .models import ParentMessage


class ParentMessageForm(forms.ModelForm):
    class Meta:
        model = ParentMessage
        fields = ["parent_name", "student_name", "message"]
        widgets = {
            "parent_name": forms.TextInput(attrs={
                "placeholder": "اسم ولي الأمر",
                "required": True,
            }),
            "student_name": forms.TextInput(attrs={
                "placeholder": "اسم الطالبة",
                "required": True,
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "اكتب رسالتك التحفيزية هنا…",
                "rows": 4,
                "required": True,
            }),
        }
