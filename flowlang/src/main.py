
import lexer
import parserr

def main():

    #read the current flow source code in test.lang and store it in variable
    content = ""
    
    with open('test.lang', 'r') as file:
        content = file.read()
    
    #
    #Lexer
    #

    #we call the lexer class and initialise it with the source code
    lex = lexer.Lexer(content)
    #we now call the tokenize method
    tokens = lex.tokenize()

    #
    #Parser
    #

    parse = parserr.Parser(tokens)
    parse.parse()

main()