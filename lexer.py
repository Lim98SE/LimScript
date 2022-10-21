from sly import Lexer

class LimScriptLexer(Lexer):
    tokens = { TOKEN_ID, TOKEN_SEPARATOR, TOKEN_NUMBER, TOKEN_ASCII, TOKEN_VAR, TOKEN_EQUALS }

    ignore = " \t\n"

    TOKEN_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    TOKEN_SEPARATOR = r';'
    TOKEN_NUMBER = r'\d+'
    TOKEN_ASCII = r'#[\x21-\x7E]'
    TOKEN_VAR = r'var'
    TOKEN_EQUALS = r'='

if __name__ == '__main__':
    data = """
    var myVariable123 = #A;
    print myVariable123;
    """

    lexer = LimScriptLexer()

    for tok in lexer.tokenize(data):
        print("type=%r, value=%r" % (tok.type, tok.value))

