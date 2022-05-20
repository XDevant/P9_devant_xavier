from django import forms


class StarRatingWidget(forms.widgets.RadioSelect):
    """
    Custom RadioSelect template in order to have all inputs and labels
    in the same div in reverse order.
    Mostly for CSS compatibility (allows to then invert the labels 
    display order and turn a previous sibling into a next sibling)
    """
    template_name = 'widgets/star_rating.html'

    def id_for_label(self, id_):
        """
        Arg : String Return : String (id)
        We make sure that the fiel label point to the div cointainer
        instead of the input by overloading this method
        """
        return id_


class ImageWidget(forms.widgets.ClearableFileInput):
    """
    A custom ClearableFileInput template for image file upload/modification
    We add the img in the rendered html if provided and hide the user agent
    download file buton.
    Note: the template container div id is the usual input id generated
    by Django(stored in _id). The template input has _id + '_0' as id.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = 'widgets/modify_uploaded_image.html'

    def id_for_label(self, id_):
        """
        Arg : String Return : String (id)
        We make sure that the fiel label point to the div cointainer
        instead of the input
        """
        return id_
