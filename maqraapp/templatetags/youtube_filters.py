from django import template

register = template.Library()

@register.filter
def youtube_embed(url):
    if "youtube.com/watch" in url:
        return url.replace("watch?v=", "embed/")
    elif "youtu.be/" in url:
        return url.replace("youtu.be/", "youtube.com/embed/")
    return url
