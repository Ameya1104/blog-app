from django import forms
from .models import Post, Category, Comment

# choices = [("Sports", "Sports"), ("Entertainment", "Entertainment"), ("Science & Technology", "Science & Technology")]
choices = Category.objects.all().values_list("name", "name")

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "header_image", "author", "category", "body")

        widgets = {
            "title" : forms.TextInput(attrs={'class': 'field', 'placeholder': 'Title Of Your Blog'}),
            "author" : forms.TextInput(attrs={'class': 'ui disabled field', 'placeholder': 'Author Of This Post', 'id': 'author'}),
            "category" : forms.Select(choices=choice_list, attrs={'class': 'field', 'placeholder': 'Category Of This Post'}),
            "body" : forms.Textarea(attrs={'class': 'field', 'placeholder': 'Your Blog'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")

        widgets = {
            "title" : forms.TextInput(attrs={'class': 'field', 'placeholder': 'Title Of Your Blog'}),
            "body" : forms.Textarea(attrs={'class': 'field', 'placeholder': 'Your Blog'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")

        widgets = {
            "name" : forms.TextInput(attrs={'class': 'field', 'placeholder': 'Your Name'}),
            "body" : forms.Textarea(attrs={'class': 'field', 'placeholder': 'Your Comment'}),
        }