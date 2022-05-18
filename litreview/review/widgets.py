from django import forms


class StarRatingWidget(forms.widgets.RadioSelect):
    """
    We want our own template in order to have
    all inputs and labels in the same div in reverse order
    By hiding the buttons and using a row reverse flex direction
    we can invert the display order and use the ~ next siblings css operator
    to display lower star ratings as if checked without JS
    """
    template_name = 'widgets/star_rating.html'

    def id_for_label(self, id_):
        """We make sure that the fiel label point to the div cointainer
        instead of the input
        """
        return id_


class ImageWidget(forms.widgets.ClearableFileInput):
    """
    A custom template for image file upload/modification
    We add the img in the rendered html if provided and
    hide the user agent download file butonn
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = 'widgets/modify_uploaded_image.html'

    def id_for_label(self, id_):
        """We make sure that the fiel label point to the div cointainer
        instead of the input
        """
        return id_
