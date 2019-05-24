
class VariableObject(object):

    def __init__(self):
        #this will hold python exec string for the variable decleration
        self.exec_string = ""

    def transpile(self, name, operator, value):
        #appends the python executable string converted using our parser
        self.exec_string += name + " " + operator + " " + value + "\n"
        return self.exec_string