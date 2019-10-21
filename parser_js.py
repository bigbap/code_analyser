from combinators import *
from grammar import INT, OPERATOR, KEYWORD, ID, COMMENT

parser = Tag(ID) + Reserved('=', OPERATOR) + Tag(INT)
comment_parser = Tag(COMMENT)