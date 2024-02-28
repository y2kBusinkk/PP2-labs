

import re


def match(input_string):

    pattern = re.compile(r'a[b]*')
    ab = pattern.search(input_string)

    if ab:
        return True

    return False


line = input()
print(match(line))


def match2(input_string):

    pattern = re.compile(r'a[bb]{2,3}')
    ab = pattern.search(input_string)

    if ab:
        return True

    return False


line = input()
print(match2(line))


def underscore(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    line = pattern.search(input_string)

    if line:
        return True

    return False


newtest = input()
print(underscore(newtest))


def case(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    line = pattern.search(input_string)

    if line:
        return True

    return False


newtest = input()
print(case(newtest))


def astartbend(input_string):
    pattern = re.compile(r'a.*b$')
    line = pattern.search(input_string)

    if line:
        return True

    return False


newtest = input()
print(astartbend(newtest))


def replacecolon(input_string):

    result = input_string.replace(' ', ':')
    result = result.replace(',', ':')
    result = result.replace('.', ':')

    return result


input_text = input()
print(replacecolon(input_text))


def snaketocamel(snakestring):

    words = snakestring.split('_')

    camelwords = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camelstring = ''.join(camelwords)

    return camelstring


input_text = input()
print(snaketocamel(input_text))


