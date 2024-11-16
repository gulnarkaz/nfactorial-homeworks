"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:
    if not my_list:
        return 0
    sorted_list = sorted(my_list)
    current = 1
    longest = 1
    for i in range(1, len(sorted_list)):
        if sorted_list[i] == sorted_list[i - 1] + 1:
            current += 1
    longest = max(longest, current)

    return longest

"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    n = len(my_list) + 1
    full_sum = n * (n + 1) // 2
    missing_sum = sum(my_list)
    return full_sum - missing_sum


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    n = len(my_list) - 1
    sum_oldlist = sum(my_list)
    sum_newlist = n * (n + 1) // 2

    return sum_oldlist - sum_newlist


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram = {}

    for word in words:
        sorted_words = str(sorted(words))

        if sorted_words not in anagram:
            anagram[sorted_words] = []

        anagram[sorted_words].append(word)

    return list(anagram.values())
