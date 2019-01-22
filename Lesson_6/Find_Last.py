# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(string, target):
    if string.find(target) == -1:
        return -1
    else:
        pos = 0
        while (string.find(target, pos + 1) != -1):
            pos = string.find(target, pos + 1)
        return pos

string = 'aaaa'
target = 'a'
pos = 0
pos =  string.find(target, pos + 1)
print pos
#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0
