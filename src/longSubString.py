"""
Find longest substring (or the length of longest substring) that has no repeated characters
"""

def no_repeat(input_string: str) -> bool:
	"""	One way to ensure a string has no repeat chars: len = # unique chars"""
	if len(input_string) == len(set(input_string)):
		return True
	else:
		return False

def longest_substring(input_string: str) -> str:
	"""
	Given a string of length n, how many substrings are there (to evaluate)?
	`n` ways to pick the first index i = n, and then j = n-1 ways to pick the end, so n*(n-1) = n^2 - n
	"""
	n = len(input_string)
	longest = '' #initialize to empty
	# go through each substring (as a slice)
	for i in range(n):
		for j in range(i+1,n+1):
			test_str = input_string[i:j]
			if no_repeat(test_str):
				if len(test_str) >= len(longest):
					longest = test_str
	#warning: Not unique, will return latest encountered
	return longest

#if program asks only for length of longest
def length_longest_substring(input_string: str) -> int:
	return len(longest_substring(input_string))