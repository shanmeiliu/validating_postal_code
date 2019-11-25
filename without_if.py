"""
Author: Charmaine Liu
Nov 24, 2019
"""

regex_integer_in_range = r"[1-9][0-9][0-9][0-9][0-9][0-9]"	# using regular expression to match 100000 to 999999

regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	#  REF  https://stackoverflow.com/questions/49325509/how-to-find-alternating-repetitive-digit-pair
'''
Explanation:

    (\d): Match and capture a digit in group #1
    (?=: Start lookahead
    \d: Match any digit
    \1: Back-reference to captured group #1
    ): End lookahead

'''
import re
print ("Please enter the postal code you want to validate")
P=input()

# using bool to validate 3 conditions
print (bool(re.match(regex_integer_in_range, P)) and len(P)==6 \
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)