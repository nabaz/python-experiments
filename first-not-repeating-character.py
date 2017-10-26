#Note: Write a solution that only iterates over the
# string once and uses O(1) additional memory, since this is what
#you would be asked to do during a real interview.

#Given a string s, find and return the first
#instance of a non-repeating character in it.
#If there is no such character, return '_'.
def firstNotRepeatingCharacter(s):
    for x in s:
        if s.count(x) == 1:
            return x
        else:
            x +=x
    return '_'

#Better solution?
    # res = "_"
    # d = {}
    # for i,c in enumerate(s):
    #     if c in d.keys():
    #         d[c] = -1
    #     else:
    #         d[c] = i
    # min_key = len(s)+1
    # for k in d.keys():
    #     if d[k]>=0:
    #         min_key = min(min_key,d[k])
    #         res = s[min_key]
    # return res

print(firstNotRepeatingCharacter("abacabad"))
