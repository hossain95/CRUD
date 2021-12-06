from django.forms import ModelForm

from . models import StudentInfo


class StudentForm(ModelForm):
    class Meta:
        model = StudentInfo
        fields = [
            "name",
            "age",
            "email",
        ]