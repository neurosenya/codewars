import re
def camel_case(string):
    """
    Converts first letters of words to uppercase
    and remove spaces between words
    """
    return re.sub(r"\s",r"", string.title())


print(camel_case("hello world"))
