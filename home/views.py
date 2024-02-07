from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home/home_page.html'

class FeaturePageView(TemplateView):
    template_name = 'home/feature_page.html'

class TestimonialPageView(TemplateView):
    template_name = 'home/testimonial_page.html'

class PricingPageView(TemplateView):
    template_name = 'home/pricing_page.html'

class FAQPageView(TemplateView):
    template_name = 'home/faq_page.html'
