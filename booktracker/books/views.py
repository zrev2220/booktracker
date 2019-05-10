from django.views.generic.base import TemplateView


# Main landing page; displays search form
class HomePageView(TemplateView):
    template_name = "search.html"
    search_options = {
        "title": "Title",
        "author_fname": "Author first name",
        "author_lname": "Author last name",
        "author_fullname": "Author full name",
    }
    contain_options = {
        "contains": "Contains",
        "startswith": "Starts With",
        "endswith": "Ends With",
        "matches": "Matches",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "Home"
        context["search_options"] = HomePageView.search_options
        context["contain_options"] = HomePageView.contain_options
        return context
