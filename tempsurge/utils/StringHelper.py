import string
import random
import re


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def rchop(string, ending):
    """
    Or re.sub(' ending$', '', string)
    """
    if string.endswith(ending):
        return string[:-len(ending)]
    return string


def lchop(string, starting):
    if string.startswith(starting):
        return string[len(starting):]
    return string


def count_words(string):
    return len(string.split())


def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None