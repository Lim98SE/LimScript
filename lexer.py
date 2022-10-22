from sly import Lexer

class LimScriptLexer(Lexer):
    tokens = {
        # Literals
        TOKEN_NUMBER,
        TOKEN_ASCII,

        # Identificator
        TOKEN_ID,
        
        # Variable types
        TOKEN_VAR,
        TOKEN_STR,
        TOKEN_ARR,

        # Control flow / Subroutines
        TOKEN_LABEL,
        TOKEN_GOTO,
        TOKEN_GOTOIF,
        
        TOKEN_SUBR,
        TOKEN_RETURN,

        # Special symbols
        TOKEN_COMP_EQUAL,
        TOKEN_COMP_NOTEQUAL,
        TOKEN_COMP_MORE,
        TOKEN_COMP_LESS,
        TOKEN_COMP_MOREEQUAL,
        TOKEN_COMP_LESSEQUAL,
     
        TOKEN_ASSIGN
    }

    literals = { '(', ')', ';' }

    ignore = ' \t'

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

    TOKEN_COMP_EQUAL = r'=='
    TOKEN_COMP_NOTEQUAL = r'!='
    TOKEN_COMP_MOREEQUAL = r'>='
    TOKEN_COMP_LESSEQUAL = r'<='
    TOKEN_COMP_MORE = r'>'
    TOKEN_COMP_LESS = r'<'

    TOKEN_ASSIGN = r'='

    TOKEN_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    TOKEN_ID['label'] = TOKEN_LABEL
    TOKEN_ID['gotoif'] = TOKEN_GOTOIF
    TOKEN_ID['goto'] = TOKEN_GOTO

    TOKEN_ID['subr'] = TOKEN_SUBR
    TOKEN_ID['return'] = TOKEN_RETURN

    TOKEN_ID['var'] = TOKEN_VAR
    TOKEN_ID['str'] = TOKEN_STR
    TOKEN_ID['arr'] = TOKEN_ARR

    ignore_comment = r'//.*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

if __name__ == '__main__':
    data = """
    subr main (
        // My program
        var myVariable123 = #=; // Create a variable called myVariable123.

        // Ok now we print it
        print myVariable123;

        // invalid command
        //printmyVariable123;

        var i = #A;

        label myLabel;

        print i;

        gotoif myLabel i <= #Z;

        mySubroutine;

        exit 0
    );

    subr mySubroutine (
        print #A; // You don't have to add indentation

        var i = 0;

        label loop;

        add i 1 i;

        gotoif subroutineEnd i > 10;

        goto loop;

        label subroutineEnd;
    );

    // Goodbye
    """

    lexer = LimScriptLexer()

    for tok in lexer.tokenize(data):
        print(tok)

