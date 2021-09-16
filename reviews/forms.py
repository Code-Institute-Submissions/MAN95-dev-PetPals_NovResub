from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ A form for users to add a review to an item """

    class Meta:
        model = Review
        exclude = (
            'user',
            'date_created',
            'item')

        fields = [
            'title',
            'description',]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Write your review here...',
        }

        # Add placeholders and classes to input fields
        self.fields['title'].widget.attrs['autofocus'] = True
       