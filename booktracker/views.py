from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            form = self.get_form()
            if not form.is_valid():
                context["username"] = form.cleaned_data["username"]
                context["password"] = form.cleaned_data["password"]
        return context
