from django import template
import logging

logger = logging.getLogger('swallowN')
register = template.Library()

@register.filter
def has_key(dictvar, key):
  return dictvar.has_key(key)
