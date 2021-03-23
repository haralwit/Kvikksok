from django.contrib.gis import forms
from.models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted']
        #author = models.ForeignKey(User, on_delete=models.CASCADE)
        geom = forms.PointField()