'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # set the count of th to 0 as we assume there isn't any in the th since we haven't searche for it
    th = 0
    
    # if th does not exist, return th which is initialized as 0
    if word.find("th") == -1:
        return th
        # otherwise, if th was found (find can only find one at a time), recursively loop over the function again replacing the th with a space so that it isn't counted again, and do it once as you have only found 1 so far.
    else:
        return 1 + count_th(word.replace("th", " ", 1))
    
