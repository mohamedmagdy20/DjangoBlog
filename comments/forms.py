from pyexpat import model
from django import forms
from comments.models import Comment
class CommentForm(forms.ModelForm):
    # model:Come
    class Meta:
        model = Comment
        fields =['comment']