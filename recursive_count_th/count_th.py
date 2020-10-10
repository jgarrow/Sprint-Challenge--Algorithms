'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    total = 0
    word_arr = list(word)
    
    # if the first 2 characters in `word` are "th", increment total
    # then call count_th again, passing in `word`, but slicing off the first two characters that we just checked

    # base case
    if len(word_arr) < 2:
        return 0
    else:
        total += count_th(''.join(word_arr[1:]))

    if ''.join(word_arr[0:2]) == "th":
        total += 1
    
    return total
