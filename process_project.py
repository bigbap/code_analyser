import json
import grammar as g
import pandas as pd
from lexer import lex
import os
from datetime import datetime
from parser_js import parser, comment_parser

def __main__():
    file = open("config.json","r")
    config = json.load(file)
    
    project_path = config["path"]
    include = config["include"] if config["include"] != None or "" else None
    exclude = config["exclude"] if config["exclude"] != None or "" else None
    # project_path = "C:\\Users\\simon.rodrigues\\Desktop\\lexer"

    token_list = []
    errors = []
    for root, dirs, files in os.walk(project_path):
        for fname in files:
            if(fname.endswith(include) and not fname.endswith(exclude)):
                with open(os.path.join(root, fname)) as code_file:
                    try:
                        code = code_file.read()
                        tokens, t_errors = lex(code, g.js(), fname)
                        for n, i in enumerate(tokens):
                            tokens[n] = (i[0], i[1], fname)
                        token_list, errors = token_list + tokens, errors + t_errors
                    except:
                        errors.append(os.path.join(root, fname))
    
    print(len(token_list))
    for i, token in enumerate(token_list):
        check = parser(token_list, i)
        if check != None:
            print(check)
        # check = comment_parser(tokens, i)
        # if check != None:
        #     print(check)

    df = pd.DataFrame(token_list, columns=["token","token_type","file"])
    df.to_csv("tokens.csv",";")

    if len(errors) > 0:
        f = open("logs\\errors.txt","a+")
        for error in errors:
            f.write("Date: %s - File: %s\n" % (datetime.now(), error))
        f.close()

if __name__ == "__main__":
    __main__()