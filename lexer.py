from sly import Lexer

class LimScriptLexer(Lexer):
    tokens = { TOKEN_NUMBER, TOKEN_ASCII, TOKEN_ID, TOKEN_PRINT, TOKEN_VAR, TOKEN_ASSIGN }

    literals = { ';' }

    ignore = ' \t'

    TOKEN_ASSIGN = r'='

    TOKEN_NUMBER = r'\d+'
    TOKEN_ASCII = r'\#[\x21-\x7E]'

    # Converting the value to an integer
    def TOKEN_NUMBER(self, t):
        t.value = int(t.value)
        return t

    def TOKEN_ASCII(self, t):
        t.value = ord(t.value[1])
        t.type = "TOKEN_NUMBER"

        return t

    TOKEN_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    ignore_comment = r'//.*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

if __name__ == '__main__':
    data = """
    // My program
    var myVariable123 = #;; // Create a variable called myVariable123.

    // Ok now we print it
    print myVariable123;

    // invalid command
    //printmyVariable123;

    // Goodbye
    """

    lexer = LimScriptLexer()

    for tok in lexer.tokenize(data):
        print(tok)

