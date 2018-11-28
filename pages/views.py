from django.views.generic import TemplateView


class MembershipPageView(TemplateView):
    template_name = 'membership.html'