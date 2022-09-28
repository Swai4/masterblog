from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
        "text": "Type Comment"
    }


class SearchForm(forms.Form):
    search_field = forms.CharField(label='search', max_length=100)

    