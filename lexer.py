import grammar as g
import os
import re

def lex(characters, grammar, fname):
    pos = 0
    tokens = []
    errors = []
    while pos < len(characters):
        match = None
        for token_expr in grammar:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag, fname)
                    tokens.append(token)
                break
        if not match:
            errors.append('Illegal character: %s at position %d. File: %s' % (characters[pos], pos, fname))
            pos += 1
        else:
            pos = match.end(0)
    return (tokens, errors)