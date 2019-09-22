"""
Find longest substring (or the length of longest substring) that has no repeated characters
"""

# Given a string of length n, how many substrings are there (to evaluate)?
# n ways to pick the first index i = n, and then j = n-1 ways to pick the end, so n*(n-1) = n^2 - n

# One way to make sure a string has no repeat chars is that the len is same as number of unique chars
def no_repeat(s):
	if len(s) == len(set(s)):
		return True
	else:
		return False

def longest_substring(input_string):
	n = len(input_string)
	longest = '' #initialize to empty
	# go through each substring
	for i in range(n):
		for j in range(i+1,n+1):
			test_str = input_string[i:j]
			if no_repeat(test_str):
				if len(test_str) >= len(longest):
					longest = test_str 
	#warning: Not unique, will return latest encountered
	return longest

#if program asks only for length of longest
def length_longest_substring(s):
	return len(longest_substring(s))