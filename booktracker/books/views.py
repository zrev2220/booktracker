from django.views.generic.base import TemplateView


# Main landing page; displays search form
class HomePageView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "Home"
        return context
