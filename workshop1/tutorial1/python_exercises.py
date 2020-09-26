"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if (x % 2) == 0:
        return False
    else:
        return True


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    # track count of repeated letters
    count = 0
    i = 0
    while i < (len(word) // 2):
        if word[i] == word[-(i + 1)]:
            count += 1
        i += 1
    if count == (len(word) // 2):
        return True
    else:
        return False


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    odd_list = []
    for i in numlist:
        if is_odd(numlist[i - 1]):
            odd_list.append(numlist[i - 1])
    return odd_list


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """

    
    
# test cases
print(is_odd(0))
print(is_odd(5))
print(is_odd(-2))
print(is_odd(-1))

print(is_palindrome("Roshni"))
print(is_palindrome("level"))
print(is_palindrome("Hannah"))
print(is_palindrome("hannah"))
print(is_palindrome("lol"))

print(only_odds([1, 2, 3, 4, 5, 6]))
print(only_odds([-2, -1, 0, 1, 2]))