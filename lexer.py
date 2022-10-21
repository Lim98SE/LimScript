from sly import Lexer

class LimScriptLexer(Lexer):
    # The order is important!
    tokens = {
        TOKEN_PRINT,
        TOKEN_VAR,
        TOKEN_ID, 
        TOKEN_ASCII,
        TOKEN_NUMBER,
        TOKEN_EQUALS,
        TOKEN_SEPARATOR
    }

    ignore = " \t\n"


    TOKEN_PRINT = r'print'
    TOKEN_VAR = r'var'
    
    TOKEN_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'


    TOKEN_ASCII = r'#[\x21-\x7E]'
    TOKEN_NUMBER = r'\d+'

    TOKEN_EQUALS = r'='
    
    TOKEN_SEPARATOR = r';'

if __name__ == '__main__':
    data = """
    var myVariable123 = #A;
    print myVariable123;
    """

    lexer = LimScriptLexer()

    for tok in lexer.tokenize(data):
        print("type=%r, value=%r" % (tok.type, tok.value))

