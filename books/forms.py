from django import forms

from books.models import Book, Author, Category
from people.models import Person


# noinspection PyPep8Naming
def AttrWidget(widget, attrs: dict = None):
    """
    Returns a Widget class, modified with Bootstrap .form-control CSS class, as well as any other given attributes.

    :param widget: Widget class reference for which to return a modified class reference.
    :param attrs: Dictionary of HTML attributes to add to the returned Widget class.
    :return: A Widget class, modified with the given attributes applied.
    """
    if attrs is None:
        attrs = {}
    # add Bootstrap .form-control
    attrs["class"] = attrs.get("class", "") + " form-control"
    return widget(
        attrs=attrs
    )


class BookForm(forms.ModelForm):
    """
    Form for Book model.
    """
    title = forms.CharField(max_length=2047, widget=AttrWidget(forms.TextInput))
    location = forms.CharField(max_length=255, required=False, widget=AttrWidget(forms.TextInput))
    notes = forms.CharField(required=False, widget=AttrWidget(forms.Textarea, {"rows": "5"}))
    return_date = forms.DateField(required=False, widget=AttrWidget(forms.DateInput, {"type": "date"}))

    author = forms.ModelMultipleChoiceField(Author.objects.all().order_by('last_name', 'first_name'), required=False,
                                            widget=AttrWidget(forms.SelectMultiple))
    category = forms.ModelMultipleChoiceField(Category.objects.all().order_by('descr'), required=False,
                                              widget=AttrWidget(forms.SelectMultiple))
    checkout = forms.ModelChoiceField(Person.objects.all().order_by('first_name', 'last_name'), required=False,
                                      widget=AttrWidget(forms.Select))

    class Meta:
        model = Book
        fields = "__all__"
