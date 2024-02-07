from wagtail import hooks, blocks
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel

@register_setting
class GlobalSEOSettings(BaseSiteSetting):
    structured_data_markup = blocks.CharBlock()
    meta_tags = blocks.CharBlock()
    social_media_tags = blocks.CharBlock()
    lazy_loading = blocks.BooleanBlock(default=True)
    ssl_certificates = blocks.BooleanBlock(default=True)
    
    panels = [
        FieldPanel('structured_data_markup'),
        FieldPanel('meta_tags'),
        FieldPanel('social_media_tags'),
        FieldPanel('lazy_loading'),
        FieldPanel('ssl_certificates'),
    ]

# Implement any other hooks or functions related to SEO tasks if needed
