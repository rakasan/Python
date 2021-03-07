import re

# characters are defined
character_1 = "Dorothy"
character_2 = "Henry"

# compile your regular expression here
regular_expression = re.compile("\w{7}")

# check for a match to character_1 here
result_1 = re.match(regular_expression,character_1)
print(result_1)


# store and print the matched text here
match_1 = result_1.group(0)


# compile a regular expression to match a 7 character string of word characters and check for a match to character_2 here
result_2 = re.match(regular_expression,character_2)
