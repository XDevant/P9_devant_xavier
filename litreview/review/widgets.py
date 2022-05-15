from django import forms
from django.utils.safestring import mark_safe

class StarRatingWidget(forms.widgets.RadioSelect):
    """We want our own template in order to have
    all inputs and labels in the same div in reverse order
    By hiding the buttons and using a row reverse flex direction
    we can invert the order again and use the ~ next siblings css operator
    to display lower star ratings as if checked without JS
    """
    template_name = 'widgets/star_rating.html'


class ImageWidget(forms.widgets.FileInput):
    """We just add the img in the rendered html if provided"""
    def render(self, name, value, attrs=None, **kwargs):
        html = super().render(name, value, attrs=attrs, **kwargs)
        if value:
            img_html = mark_safe(
                f'<img src="{value.url}"/>')
            return f'{img_html} {html}'
        return html