from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.blocks import ImageChooserBlock
class HomePage(Page):
    hero_section = StreamField([
        ('call_to_action', blocks.StructBlock([
            ('text', blocks.CharBlock()),
            ('url', blocks.URLBlock()),
        ])),
        ('feature', blocks.StructBlock([
            ('icon', blocks.CharBlock()),
            ('title', blocks.CharBlock()),
            ('description', blocks.TextBlock()),
            ('call_to_action', blocks.StructBlock([
                ('text', blocks.CharBlock()),
                ('url', blocks.URLBlock()),
            ])),
        ])),
        ('demo', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('description', blocks.TextBlock()),
        ])),
        # Add other blocks as needed
    ], use_json_field=True, default=[
        {
            'type': 'feature',
            'value': {
                'icon': 'fa-cogs',
                'title': 'Powerful Features',
                'description': 'Discover the amazing features that make NexusTech stand out.',
                'call_to_action': {
                    'text': 'Learn More',
                    'url': '/features/',
                },
            },
        },
        {
            'type': 'call_to_action',
            'value': {
                'text': 'Join Now',
                'url': '/signup/',
            },
        },
    ])
    
    sticky_navigation_menu = StreamField([
        ('link', blocks.StructBlock([
            ('text', blocks.CharBlock()),
            ('url', blocks.URLBlock()),
        ])),
        # Add other blocks as needed
    ], use_json_field=True, default=[
        {
            'type': 'link',
            'value': {
                'text': 'Home',
                'url': '/',
            },
        },
    ])

    content_panels = Page.content_panels + [
        FieldPanel('hero_section'),
        FieldPanel('sticky_navigation_menu'),
    ]

# Create other models similar to HomePage
class FeaturePage(Page):
    icon = models.CharField(max_length=255)
    description = RichTextField()
    demo = StreamField([
        ('demo', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('description', blocks.TextBlock()),
        ])),
    ], use_json_field=True)
    call_to_action = StreamField([
        ('call_to_action', blocks.StructBlock([
            ('text', blocks.CharBlock()),
            ('url', blocks.URLBlock()),
        ])),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('icon'),
        FieldPanel('description'),
        FieldPanel('demo'),
        FieldPanel('call_to_action'),
    ]

class TestimonialPage(Page):
    author_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    testimonial_text = RichTextField()
    image = models.ImageField(upload_to='testimonials/')

    content_panels = Page.content_panels + [
        FieldPanel('author_name'),
        FieldPanel('position'),
        FieldPanel('testimonial_text'),
        FieldPanel('image'),
    ]

class PricingPage(Page):
    pricing_plans = StreamField([
        ('pricing_plan', blocks.StructBlock([
            ('name', blocks.CharBlock()),
            ('price', blocks.DecimalBlock()),
            ('features', blocks.ListBlock(blocks.CharBlock())),
        ])),
    ], use_json_field=True)
    feature_comparison_table = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('pricing_plans'),
        FieldPanel('feature_comparison_table'),
    ]

class FAQPage(Page):
    collapsible_sections = StreamField([
        ('section', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('faqs', blocks.ListBlock(blocks.StructBlock([
                ('question', blocks.CharBlock()),
                ('answer', blocks.TextBlock()),
            ]))),
        ])),
    ], use_json_field=True)
    searchable_faqs = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('collapsible_sections'),
        FieldPanel('searchable_faqs'),
    ]