"""
this is an illustration of a function that 
that returns a tuple with the length of a 
string and its first character.
- Prototype: def multiple_returns(sentence):
- If the sentence is empty, the first character should be equal to None
- You are not allowed to import any module
"""
def multiple_returns(sentence):
    if len(sentence) != 0:
        result = (len(sentence), sentence[0])
    else:
        result = (len(sentence), 'None')

    return result

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))


sentence = "Holberton"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))


sentence = "Holberton is so cool"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))


sentence = "H"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))


sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))