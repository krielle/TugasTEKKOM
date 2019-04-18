class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])

            self.token_index += 1

    def parse_variable_declaration(self, token_stream):
        tokens_checked = 0

        for token in range(0, len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            if token == 0:
                print('Variable type: '+token_value)

            elif token == 1 and token_type == "IDENTIFIER":
                print('Variable name: '+token_value)
            elif token == 1 and token_type != "IDENTIFIER":
                print("Error: Invalid variable name '" +token_value + "'")
                quit()

            elif token == 2 and token_type == "OPERATOR":
                print('Assignment Operator: '+token_value)
            elif token == 2 and token_type != "OPERATOR":
                print("Error: Assignment Operator is missing or invalid it should be '='")
                quit()

            elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print('Variable Value: '+token_value)
            elif token == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print("Invalid variable assignment value '" +token_value + "'")
                quit()

            tokens_checked += 1

        self.token_index += tokens_checked
