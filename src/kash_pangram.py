def is_p(s):
	return not set('abcd') - set(s.lower())

print(is_p('ac'))

print(is_p('abcd'))

is_p2 = lambda s: not set('abcd') - set(s.lower())
print(is_p2('abcd'))

