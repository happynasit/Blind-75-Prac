class Solution:
    def isValid(self, s: str) -> bool:
        
        opening_parenthesis = []
        opening_brackets = ('(', '[', '{')
        for letter in s:
            if letter in opening_brackets:
                opening_parenthesis.append(letter)
            else:
                if not opening_parenthesis:
                    return False
                if letter == ')' and opening_parenthesis[-1] == '(':
                    opening_parenthesis.pop()
                elif letter == ']' and opening_parenthesis[-1] == '[':
                    opening_parenthesis.pop()
                elif letter == '}' and opening_parenthesis[-1] == '{':
                    opening_parenthesis.pop()
                else:
                    return False
        return opening_parenthesis == []
            
