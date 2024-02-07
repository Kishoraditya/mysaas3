from django.urls import path
from .views import HomePageView, FeaturePageView, TestimonialPageView, PricingPageView, FAQPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('feature/', FeaturePageView.as_view(), name='feature'),
    path('testimonial/', TestimonialPageView.as_view(), name='testimonial'),
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('faq/', FAQPageView.as_view(), name='faq'),
    # Add other URL patterns as needed
]
