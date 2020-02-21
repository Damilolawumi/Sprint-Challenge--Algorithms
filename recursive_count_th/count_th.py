'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

mine

- check if word is less than 2
- if it doesn't exist end program
-. compare letters in word two at a time to see if it satifies condition
-. if step two returns True add + 1 else count + 0
-. remove one letter at a time from word
-. repeat
'''
def count_th(word):
    # if initial word is less than 2 words, return 0
    # because it won't be possible for the word
    # to be "th"
    if len(word) < 2:
        return 0
    
    # If first two indexes contain 'th", add one to the count - skip over the first index and compare next two adjacent indexes

    elif word[:2] =='th':
        return count_th(word[1:]) + 1

     # If first two indexes dont contain 'th', just skip over the first index and compare next two adjacent indexes

    else:
         
        return count_th(word[1:])        

print(count_th('theostht'))

 
