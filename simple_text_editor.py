"""
This program implements a simple text editor. Initially, your editor contains an empty string, S.
You must perform Q operations of the following 4 types:

1. append(W) - Append string W to the end of S .
2. delete(k) - Delete the last k characters of S .
3. print(k)  - Print the kth character of S.
4. undo()    - Undo the last (not previously undone) operation of type 1 or 2,
               reverting S to the state it was in prior to that operation.

Author: Aditya Dubal
Language: Python 2.7
"""


class TextEditor:

    def __init__(self):
        """
            items[]           - list to keep track of last operations
            result_string     - initial empty string
        """
        self.result_string = ''
        self.items = ['']

    def add_end(self, word_string):
        # Append word at the end of empty string
        self.items.append(self.result_string + word_string)
        return self.result_string + word_string

    def delete(self, no_chars):
        # Delete last k characters by slicing
        self.result_string = self.result_string[: -no_chars]
        self.items.append(self.result_string)

    def undo(self):
        # Undo the last operation
        self.items.pop()
        self.result_string = self.items[-1]


if __name__ == '__main__':
    print 'Enter number of operations'
    # Number should be of type int
    try:
        total_number = int(raw_input())
    except:
        raise ValueError('Input must be int value')

    TextEditor_Obj = TextEditor()   # Instantiation

    # loop for each query
    for _ in range(total_number):
        print 'Enter operation with given format'
        input_string = raw_input().split(' ')
        operation_number = int(input_string[0])

        # Value should be in range of 1 to 4 inclusive
        assert 1 <= operation_number <= 4, 'Invalid operation format'

        if operation_number == 1:
            TextEditor_Obj.result_string = TextEditor_Obj.add_end(input_string[1])

        elif operation_number == 2:
            try:
                TextEditor_Obj.delete(int(input_string[1]))
            except:
                raise ValueError('Entered invalid index for given length of string')

        elif operation_number == 3:
            try:
                print 'k th character of resultant string is: ', TextEditor_Obj.result_string[int(input_string[1]) - 1]
            except:
                raise ValueError('Entered index not in string')

        elif operation_number == 4:
            try:
                TextEditor_Obj.undo()
            except:
                raise ValueError('No operation to undo')
