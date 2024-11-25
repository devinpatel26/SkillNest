from django.template.loader import get_template
from django.utils.html import format_html

def get_cloudinary_image_object(instance,
                                field_name='image',
                                as_html=False,
                                width=1200):
    if not hasattr(instance, field_name):
        return ''
    image_object = getattr(instance, field_name, None)
    if not image_object:
        return ''
    image_option = {'width': width}
    if as_html:
        return image_object.image(**image_option)
    url = image_object.build_url(**image_option)
    return url


video_html = """

"""


def get_cloudinary_video_object(instance,
                                field_name='video',
                                as_html=False,
                                width=None,
                                height=None,
                                sign_url=False,
                                fetch_format="auto",
                                quality="auto",
                                controls=True,
                                autoplay=True):
    if not hasattr(instance, field_name):
        return ''
    
    video_object = getattr(instance, field_name, None)
    if not video_object:
        return ''
    
    # Video transformation options
    video_option = {
        'sign_url': sign_url,
        'fetch_format': fetch_format,
        'quality': quality,
    }
    if controls:
        video_option['controls'] = controls
    if autoplay:
        video_option['autoplay'] = autoplay
    if width is not None:
        video_option['width'] = width
    if height is not None:
        video_option['height'] = height
    if height and width:
        video_option['crop'] = 'limit'
    
    # Generate video URL
    url = video_object.build_url(**video_option)
    
    # If as_html is True, render an <iframe> or <video> tag
    if as_html:
        # Template rendering
        template_name = 'video\snippets\embed.html'
        try:
            tmpl = get_template(template_name)
            rendered_html = tmpl.render({'video_url': url})
            return format_html(rendered_html)  # Ensure HTML is safe
        except Exception as e:
            return f"Error loading template: {e}"
    
    # Return plain URL if `as_html` is False
    return url




  