"""
    # @file                : python_programs1.py
    # Program Description  : python programs to modify existing string
    # Date         : 3rd May 2023
"""

class pythonPrograms():
    """
    Different Python Programs on strings
    """
    def __init__(self, string):
        self.string = string
        self.modified_string = ""

    def remove_space_from_string(self):
        """
        This function removes spaces from a given sentence
        :return:
        """
        for each_char in self.string:
            if each_char == " ":
                print("space removed")
            else:
                self.modified_string+=each_char
        return self.modified_string

    def reverse_string(self):
        """
        This function removes spaces from a given sentence
        :return:
        """
        self.modified_string = ""
        for each_char in self.string:
            self.modified_string = each_char + self.modified_string
        return self.modified_string

classobj = pythonPrograms("Hello World")
output = classobj.remove_space_from_string()
print(output)
print("\n")
output2 = classobj.reverse_string()
print(output2)





