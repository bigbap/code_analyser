KEYWORD =   "KEYWORD"
OPERATOR =  "OPERATOR"
TYPE =      "TYPE"
ID =        "ID"
COMMENT =   "COMMENT"
STRING =    "STRING"
INT =       "INT"
BLOCK =     "BLOCK"
SEPARATOR = "SEPARATOR"

def js():
    return [
        (r'[ \n\t]+',                   None),
        (r'/\*(.|[\\r\\n])*?\*/',       COMMENT),
        (r'//(.*?)\n',                  COMMENT),
        (r'([\'"])(.*?)\1',             STRING),
        (r'([\+\-\*\/\=<>\|\&!\?:%])',  OPERATOR),
        (r'[\.,;]',                     SEPARATOR),
        (r'[\{\}\[\]\(\)]',             BLOCK),
        (r'class',                      KEYWORD),
        (r'function',                   KEYWORD),
        (r'var',                        KEYWORD),
        (r'namespace',                  KEYWORD),
        (r'private',                    KEYWORD),
        (r'public',                     KEYWORD),
        (r'if',                         KEYWORD),
        (r'else',                       KEYWORD),
        (r'while',                      KEYWORD),
        (r'do',                         KEYWORD),
        (r'for',                        KEYWORD),
        (r'new',                        KEYWORD),
        (r'int',                        TYPE),
        (r'null',                       TYPE),
        (r'string',                     TYPE),
        (r'void',                       TYPE),
        (r'byte',                       TYPE),
        (r'[0-9]+',                     INT),
        (r'[A-Za-z$_][A-Za-z0-9_\-$]*', ID),
    ]

def csharp():
    return [
        (r'[ \n\t]+',                   None),
        (r'/\*(.|[\\r\\n])*?\*/',       COMMENT),
        (r'//(.*?)\n',                  COMMENT),
        (r'([\'"])(.*?)\1',             STRING),
        (r'([\+\-\*\/\=<>\|\&!\?:%])',  OPERATOR),
        (r'[\.,;]',                     SEPARATOR),
        (r'[\{\}\[\]\(\)]',             BLOCK),
        (r'class',                      KEYWORD),
        (r'namespace',                  KEYWORD),
        (r'private',                    KEYWORD),
        (r'public',                     KEYWORD),
        (r'protected',                  KEYWORD),
        (r'using',                      KEYWORD),
        (r'if',                         KEYWORD),
        (r'else',                       KEYWORD),
        (r'while',                      KEYWORD),
        (r'do',                         KEYWORD),
        (r'for',                        KEYWORD),
        (r'new',                        KEYWORD),
        (r'int',                        TYPE),
        (r'null',                       TYPE),
        (r'string',                     TYPE),
        (r'void',                       TYPE),
        (r'byte',                       TYPE),
        (r'[0-9]+',                     INT),
        (r'[A-Za-z$_][A-Za-z0-9_\-$]*', ID),
    ]