from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def send_email(subject, template, from_email, to, context):
    plaintext = get_template(template + ".txt")
    html = get_template(template + ".html")

    c = Context(context)

    text_content = plaintext.render(c)
    html_content = html.render(c)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()