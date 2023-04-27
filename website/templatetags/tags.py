from django import template
from datetime import datetime

register = template.Library()
 
"""
{% upper %}This will appear in uppercase, {{ your_name }}.{% endupper %}

{% modal %}
    <h1>Look ma! I'm in a modal!</h1>
{% endmodal %}


"""
@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

@register.tag
def modal(parser, token):
    nodelist = parser.parse(('endmodal',))
    parser.delete_first_token()
    return ModalNode(nodelist)
 
class ModalNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        return output