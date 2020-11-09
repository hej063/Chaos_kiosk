from django import forms
from .models import Post, Card

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('count',)

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('photo',)
