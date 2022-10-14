from django.shortcuts import redirect, render

from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect("contents")

        return super().dispatch(request, *args, **kwargs)


class ContentView(TemplateView):
    template_name = "contents/main.html"