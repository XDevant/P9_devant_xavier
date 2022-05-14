from django import forms
from django.utils.safestring import mark_safe

class StarRatingWidget(forms.widgets.RadioSelect):
    template_name = 'widgets/star_rating.html'


class ImageWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        html = super().render(name, value, attrs=attrs, **kwargs)
        if value:
            img_html = mark_safe(
                f'<img src="{value.url}"/>')
            return f'{img_html} {html}'
        return html