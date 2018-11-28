import hashlib
import urllib
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    # default = "https://example.com/static/images/defaultavatar.jpg"
    # return "https://www.gravatar.com/avatar/%s?%s" % (
    # hashlib.md5(email.lower()).hexdigest(), urllib.parse.urlencode({'d': default, 's': str(size)}))
    return "https://www.gravatar.com/avatar/%s" % (
    hashlib.md5(email.lower()).hexdigest())


# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email.encode('utf-8'), size)
    return mark_safe('<img src="%s" height="%d" width="%d" class="author-thumb" alt="Author Image">' % (url, size, size))