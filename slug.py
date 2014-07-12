import unicodedata

def allowed(character):
    return unicodedata.category(character).startswith('L')

def slugify(text, allowed=allowed, substitute="-"):
    """Remove unallowed characters from text by replacing them with
    the given substition character."""
    # Borrowed from http://stackoverflow.com/a/9042688/1550074
    class D(dict):
        def __getitem__(self, key):
            return key if allowed(chr(key)) else substitute
    return text.translate(D()).lower()
