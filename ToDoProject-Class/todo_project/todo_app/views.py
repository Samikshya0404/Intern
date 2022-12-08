from django.views.generic import TemplateView

class StaticView(TemplateView):
   template_name = "base.html"