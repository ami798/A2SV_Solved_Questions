t=int(input())
n=list(map)
def can_form_another_palindrome(s):
	from collections import Counter
	n = len(s)
	freq = Counter(s)
	odd_count = sum(1 for v in freq.values() if v % 2 == 1)
	# A string can be rearranged into a palindrome if odd_count <= 1
	# But we need ANOTHER palindrome, not the same as original
	# If all characters are the same, or only one possible palindrome, answer is NO
	# If there are at least 2 different characters, and can form a palindrome, answer is YES
	if n == 2:
		# Only two chars, must be different to form another palindrome
		return "YES" if s[0] != s[1] else "NO"
	if odd_count > 1:
		return "NO"
	# If all characters are the same, only one palindrome possible
	if len(set(s)) == 1:
		return "NO"
	# If the string is already a palindrome, check if there is another arrangement
	# If not a palindrome, then any palindrome arrangement is another
	if s != s[::-1]:
		return "YES"
	# If already a palindrome, check if there is another palindrome arrangement
	# Try to swap any two different characters
	for i in range(n):
		for j in range(i+1, n):
			if s[i] != s[j]:
				t = list(s)
				t[i], t[j] = t[j], t[i]
				if t == t[::-1]:
					continue
				# If after swap, still a palindrome, skip
				# If not, then we found another palindrome
				return "YES"
	return "NO"

t = int(input())
for _ in range(t):
	s = input().strip()
	print(can_form_another_palindrome(s))