from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.snippets.models import register_snippet
from wagtail.images.blocks import ImageChooserBlock

@register_snippet
class SiteSettings(models.Model):
    primary_color = models.CharField(max_length=7, default='#007BFF')  # Add validators for color codes
    secondary_color = models.CharField(max_length=7, default='#6c757d')
    accent_color = models.CharField(max_length=7, default='#FFD300')
    background_color = models.CharField(max_length=7, default='#F8F9FA')
    font_header = models.CharField(max_length=255, default='Roboto, Bold/Black')
    font_body = models.CharField(max_length=255, default='Open Sans, Regular/Light')
    logo = models.ImageField(upload_to='site_settings/')
    favicon = models.ImageField(upload_to='site_settings/')

    panels = [
        FieldPanel('primary_color'),
        FieldPanel('secondary_color'),
        FieldPanel('accent_color'),
        FieldPanel('background_color'),
        FieldPanel('font_header'),
        FieldPanel('font_body'),
        FieldPanel('logo'),
        FieldPanel('favicon'),
    ]

    def __str__(self):
        return "Site Settings"

@register_snippet
class SEOSettings(models.Model):
    structured_data_markup = models.TextField()
    meta_tags = models.TextField()
    social_media_tags = models.TextField()
    lazy_loading = models.BooleanField(default=True)
    ssl_certificates = models.BooleanField(default=True)

    panels = [
        FieldPanel('structured_data_markup'),
        FieldPanel('meta_tags'),
        FieldPanel('social_media_tags'),
        FieldPanel('lazy_loading'),
        FieldPanel('ssl_certificates'),
    ]

    def __str__(self):
        return "SEO Settings"

@register_snippet
class AccessibilitySettings(models.Model):
    contrast_ratios = models.TextField()
    alt_tags_for_images = models.BooleanField(default=True)
    keyboard_navigation = models.BooleanField(default=True)

    panels = [
        FieldPanel('contrast_ratios'),
        FieldPanel('alt_tags_for_images'),
        FieldPanel('keyboard_navigation'),
    ]

    def __str__(self):
        return "Accessibility Settings"


class CallToActionButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock()
    url = blocks.URLBlock()
    background_color = blocks.CharBlock()

class FeatureBlock(blocks.StructBlock):
    icon = blocks.CharBlock()
    title = blocks.CharBlock()
    description = blocks.TextBlock()
    call_to_action = CallToActionButtonBlock()

class DemoBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    description = blocks.TextBlock()

class TestimonialBlock(blocks.StructBlock):
    author_name = blocks.CharBlock()
    position = blocks.CharBlock()
    testimonial_text = blocks.TextBlock()
    image = ImageChooserBlock()

class PricingPlanBlock(blocks.StructBlock):
    plan_name = blocks.CharBlock()
    price = blocks.DecimalBlock()
    features = blocks.StreamBlock([
        ('feature', blocks.CharBlock())
    ])

class FAQSectionBlock(blocks.StructBlock):
    section_title = blocks.CharBlock()
    faqs = blocks.StreamBlock([
        ('faq', blocks.StructBlock([
            ('question', blocks.CharBlock()),
            ('answer', blocks.TextBlock()),
        ])),
    ])
