from django.core.exceptions import ValidationError

def URLValidator():
    def f(url):
        if url.startswith("http://"):
            return
        if url.startswith("https://"):
            return
        raise ValidationError

    return f
