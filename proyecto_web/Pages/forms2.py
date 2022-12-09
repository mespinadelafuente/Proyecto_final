from django import forms
from Pages.models import Post
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )



 
 
class PostForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del post",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "post-name",
                "placeholder": "Nombre de post",
                "required": "True",
            }
        ),
    )
 
    code = forms.IntegerField(
        label="Código:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "post-code",
                "placeholder": "Código del post",
                "required": "True",
            }
        ),
    )
 
    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )
 
    image = forms.ImageField()
 
    class Meta:
        model = Post
        fields = ["name", "code", "description", "image"]
 
 
