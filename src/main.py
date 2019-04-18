import lexer
import parser

def main():
    content=""
    with open('test.lang','r') as file:
        content = file.read()

    lex = lexer.Lexer(content)
    tokens = lex.tokenize()

    parse = parser.Parser(tokens)
    parse.parse()

main()