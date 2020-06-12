import json

from django.contrib import messages
from django.db.models import Q, F, Func, Value
from django.http import JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateView

from books.forms import BookForm
from .models import Author, Book, Category

# TODO: Move to a JSON file which configures this stuff?
FILTER_DICT = {
    "title": {
        "desc": "Title",
        "op": "title",
    },
    "author-last": {
        "desc": "Author (Last)",
        "op": "author__last_name",
    },
    "author-first": {
        "desc": "Author (First)",
        "op": "author__first_name",
    },
    "author-whole": {
        "desc": "Author (First+Last)",
        "op": "author_whole_name",  # requires annotation to be added to queryset to concatenate names
    },
}
MATCH_DICT = {
    "contains": {
        "desc": "Contains",
        "op": "icontains",
    },
    "startswith": {
        "desc": "Starts With",
        "op": "istartswith",
    },
    "endswith": {
        "desc": "Ends With",
        "op": "iendswith",
    },
    "matches": {
        "desc": "Matches",
        "op": "iexact",
    },
}


class HomePageView(TemplateView):
    """
    Main landing page.

    Displays search form.
    """
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        authors = sorted([{
            "id": a.id,
            "name": f"{a.last_name}{', ' if a.last_name and a.first_name else ''}{a.first_name}",
        } for a in Author.objects.all()], key=lambda a: a["name"])
        categories = [{
            "id": c.id,
            "name": c.descr,
        } for c in Category.objects.all().order_by("descr")]

        context = super().get_context_data(**kwargs)
        context["current_page"] = "Home"
        context["filter_options"] = FILTER_DICT
        context["match_options"] = MATCH_DICT
        context["authors"] = authors
        context["categories"] = categories
        return context


def book_search(request):
    """
        AJAX book search endpoint.

        Performs search given certain filters and returns results in JSON in the following structure::

            {
                "id": int,
                "title": string,
                "author_first": string,
                "author_last": string,
                "checkout": boolean,
                "location": string,
            }[]

        :param request: Request object from AJAX request.
        :return: JSON list of search results.
        """
    # TODO: try to hack this with Postman and harden it
    # TODO: add paging
    # TODO: after paging, allow retrieving all records
    # get selected filters
    filters = set(json.loads(request.POST['activeFilters']))
    combine = (lambda p, q: p & q) if request.POST['andOr'] == "and" else (lambda p, q: p | q)

    # for each filter, create Q object
    empty = True
    query = Q()
    for f in filters:
        value = request.POST[f].strip()
        if value == "":
            continue
        empty = False
        match_policy = MATCH_DICT[request.POST[f"{f}-match"]]["op"]
        kwargs = {f"{FILTER_DICT[f]['op']}__{match_policy}": value}
        query = combine(query, Q(**kwargs))

    response = []
    if not empty:
        # from https://stackoverflow.com/a/45137351/6548555
        results = Book.objects
        if "author-whole" in filters:
            # add first+last field
            results = results.annotate(author_whole_name=Func(Value(' '), F(FILTER_DICT['author-first']['op']),
                                                              F(FILTER_DICT['author-last']['op']),
                                                              function="CONCAT_WS"))
        results = results.filter(query).order_by('title')
        response = [{
            "id": obj.id,
            "title": obj.title,
            "author_first": obj.author.all()[0].first_name if len(obj.author.all()) > 0 else None,
            "author_last": obj.author.all()[0].last_name if len(obj.author.all()) > 0 else None,
            "checkout": obj.checkout is not None,  # send boolean, not name
            "location": obj.location,
        } for obj in results.all()]

    return JsonResponse({"items": response})


class AddBookView(CreateView):
    """
    Page containing a form to create a book object.
    """
    model = Book
    form_class = BookForm

    def get_success_url(self):
        if self.request.POST.get('save+add'):
            return reverse('add-book')
        else:
            return reverse('books-search')

    def form_valid(self, form):
        messages.success(self.request, f'Added "{self.request.POST.get("title")}"')
        return super().form_valid(form)


class BookDetailView(DetailView):
    """
    Page details about a book object.
    """
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['overdue'] = timezone.now().date() > self.object.return_date if self.object.return_date else False
        return context
