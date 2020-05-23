"""在Login.html中显示用户头像的自定义过滤器"""
from django import template

register = template.Library()  # 表示这是一个可用的标签库


@register.filter
def user_head_filter(user_name):
    """返回用户名第一个字符"""
    return str(user_name)[0].upper()
