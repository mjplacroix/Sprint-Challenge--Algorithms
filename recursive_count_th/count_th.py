'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    # # track how many th you encounter
    # word = word
    # th = "th"
    # count = 0
    # while th in word:
    #     print("before: ",word)
    #     count += 1
    #     word = word.replace('th', '--', 1)
    #     print("after: ", word)

    # return count

    # # track how many th you encounter
    # th = "th"
    # if th in word:
    #     count += 1
    #     print(word)
    #     word = word.replace('th', '--', 1)
    #     print(word)
    #     count_th(word, count)
    # else:
    #     """ can't figure out why count is printing the correct answer, but returning "None" """
    #     print("X: ", count)
    #     return count
    
    if len(word) > 1:
        if word[0:2] == "th":
            word = word.replace('th', '', 1)
            print(word)
            return count_th(word, count + 1)
        else:
            word = word[1:]
            print(word)
            return count_th(word, count)
    else:
        return count
