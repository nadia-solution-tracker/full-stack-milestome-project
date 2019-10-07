from django import forms
from .models import Review


class ReviewForm( forms.ModelForm ):
    RATING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":25}))
    rating = forms.Select(choices=RATING_CHOICES)

    class Meta:
        model = Review
        fields = ('comment', 'rating')