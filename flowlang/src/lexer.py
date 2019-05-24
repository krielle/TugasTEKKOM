
import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
    
       #where all the tokens created by lexer will be started
        tokens = []

       #create a word list of the source code
        source_code = self.source_code.split()

       #this will keep track of the world index we are at in source code
        source_index = 0

        #loop through each word in source code to generate tokens
        while source_index < len(source_code):
        
           word = source_code[source_index]

            #this will recognize variable and create token for it
           if word == "var": tokens.append(["VAR_DECLERATION", word])

           #this will recognize word and create token for it    
           elif re.match('[a-z]', word) or re.match('[A-Z]', word):
               if word[len(word) - 1] == ";":
                   tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
               else:
                   tokens.append(['IDENTIFIER', word])

           #this will recognize integer and create token for it 
           elif re.match('[0-9]', word):
               if word[len(word) - 1] == ";":
                   tokens.append(['INTEGER', word[0:len(word) - 1]])
               else:
                   tokens.append(['INTEGER', word])

           #this will recognize operator and create token for it 
           elif word in "=/*=-+":
               tokens.append(['OPERATOR', word])

           #if statement end ';' found then add statement end token
           if word[len(word) - 1] == ";":
               tokens.append(['STATEMENT_END', ';'])    

            #increase word index after checking it
           source_index += 1

        print(tokens)

        #return created tokens
        return tokens