from django.views.generic.base import TemplateView
from django.db.models import Q, F, Func, Value
from .models import Book
import json

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


# Main landing page; displays search form
class HomePageView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "Home"
        context["filter_options"] = FILTER_DICT
        context["match_options"] = MATCH_DICT
        return context


# AJAX search endpoint
# Performs search given certain filters and returns results in JSON
# TODO: try to hack this with Postman and harden it
def search(request):
    # get selected filters
    filters = set(json.loads(request.POST['activeFilters']))
    combine = (lambda p, q: p & q) if request.POST['andOr'] == "and" else (lambda p, q: p | q)

    # for each filter, create Q object
    query = Q()
    for f in filters:
        value = request.POST[f]
        match_policy = MATCH_DICT[request.POST[f"{f}-match"]]["op"]
        kwargs = {f"{FILTER_DICT[f]['op']}__{match_policy}": value}
        query = combine(query, Q(**kwargs))

    # from https://stackoverflow.com/a/45137351/6548555
    results = Book.objects
    if "author-whole" in filters:
        # add first+last field
        results = results.annotate(author_whole_name=Func(Value(' '), F(FILTER_DICT['author-first']['op']),
                                                          F(FILTER_DICT['author-last']['op']), function="CONCAT_WS"))
    results = results.filter(query)
    print(results)

    return ""
