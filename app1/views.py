from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
class HomePageView(TemplateView):
    template_name = 'home.html'