from django.shortcuts import render

errtitles = {
    "400": "Bad Request",
    "403": "Permission Denied",
    "404": "Page Not Found",
    "500": "Server Error",
}
errmsgs = {
    "400": "What was that? You gotta format the HTTP the right way, dude.",
    "403": "Um, no. You can't go there, you lowly peasant with no special permissions.",
    "404": "That page doesn't exist. Please go back and visit a page that exists.",
    "500": "Oh wow--a transistor blew on our end or something. Well, just hope it doesn't happen again...",  # noqa E501
}


def render_error(request, status_code):
    context = {
        "current_page": "Error",
        "status_code": status_code,
        "errtitle": errtitles.get(status_code, "OK"),
        "errmsg": errmsgs.get(
            status_code, "How is that an error? Seems like everything is fine."
        ),
    }
    return render(request, "error.html", context, "text/html", status_code)


def error400(request, exception):
    return render_error(request, "400")


def error403(request, exception):
    return render_error(request, "403")


def error404(request, exception):
    return render_error(request, "404")


def error500(request):
    return render_error(request, "500")
