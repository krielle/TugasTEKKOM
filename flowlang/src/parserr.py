
from Objects.varObject import VariableObject

class Parser(object):

    def __init__(self, tokens):

        #this will hold all tokens created
        self.tokens = tokens
        #this will hold token index we parsing at
        self.token_index = 0
        self.transpiled_code = ""

    def parse(self):

        while self.token_index < len(self.tokens):
            #hold the type of token (identifier etc.)
            token_type = self.tokens[self.token_index][0]
            #token the value of token (var etc.)
            token_value = self.tokens[self.token_index][1]

            #this trigger when var_decleration found
            if token_type == "VAR_DECLERATION" and token_value == "var":
                self.parse_variable_decleration(self.tokens[self.token_index:len(self.tokens)])

            #increment token index by 1 so we can loop through next tokens
            self.token_index += 1
        
        print(self.transpiled_code)
    
    def parse_variable_decleration(self, token_stream):

        tokens_checked = 0

        name     = ""
        operator = ""
        value    = ""

        for token in range(0, len(token_stream)):

            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            #if statement end found break out of loop as we have parsed variable decleration
            if token_type == "STATEMENT_END": break

            #this will get variable name and perform error validation for invalid name
            elif token == 1 and token_type == "IDENTIFIER":
                name = token_value
            elif token == 1 and token_type != "IDENTIFIER":
                print("ERROR: Invalid variable name '" + token_value + "'")
                quit()

            #this will get variable assignment operator e.g = or in future += and error validation
            elif token == 2 and token_type == "OPERATOR":
                operator = token_value
            elif token == 2 and token_type != "OPERATOR":
                print("ERROR: Assignment Operator is missing or invalid it should be '='")
                quit()

            #this will get the variable value assigned
            elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
                value = token_value
            elif token == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print("Invalid variable assignment value '" + token_value + "'")
                quit()

            tokens_checked += 1

        varObj = VariableObject()
        self.transpiled_code += varObj.transpile(name, operator, value)

        #increment token index by amount of token checked so we dont check them again
        self.token_index += tokens_checked