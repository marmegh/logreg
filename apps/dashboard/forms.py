from django import forms

class Post(forms.Form):
    Post = forms.CharField(label='Post', widget = forms.TextInput)
class Comment(forms.Form):
    comment = forms.CharField(label = "Comment", max_length = 255)