from .models import Comment

from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

        # Customizing feilds with  django widget
        widgets = {
            "body": forms.TextInput(
                attrs={
                    "placeholder": "Add your comment here...",
                    "class": "h-full-width h-remove-bottom",
                }
            ),
        }
