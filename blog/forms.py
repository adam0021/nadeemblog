from django import forms
from blog.models import Post,comment


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','image','content',]



class commentform(forms.ModelForm):
	class Meta:
		model=comment
		fields=['text']
