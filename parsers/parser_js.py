def parse_vars(token_list):
    var_list = []
    for i, token in enumerate(token_list):
        if token[1] == "KEYWORD" and token[0] == "var":
            var_list.append(token_list[i+1])

    return var_list

def parse_comments(token_list):
    return [a[0] for a in token_list if a[1] == "COMMENT"]