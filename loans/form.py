from django import forms
from loans.models import Post


class LoanForm(forms.ModelForm):
    post = forms.IntegerField()
    class Meta:
        model = Post
        fields = ('post',)