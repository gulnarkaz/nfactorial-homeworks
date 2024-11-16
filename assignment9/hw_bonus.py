"""
💎rite a function "two_sum(nums: list, target: int) -> tuple" that takes a list of integers
and a target integer. It should return a tuple of two indices whose elements add up to the target.
Assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
two_sum([2, 7, 11, 15], 9) -> (0, 1)
"""

def two_sum(nums: list, target: int) -> tuple:
    index_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return (index_map[complement], index)
        index_map[num] = index
    return ()

"""
💎 Exercise-2: Isomorphic Strings
Write a function "is_isomorphic(s: str, t: str) -> bool" that takes two strings s and t
and determines if they are isomorphic. Two strings s and t are isomorphic if the characters
in s can be replaced to get t, and all characters in s map to exactly one character in t and vice versa.

Example:
is_isomorphic('egg', 'add') -> True
"""

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    mapping = {}
    for char_s, char_t in zip(s, t):
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            mapping[char_s] = char_t

    reverse_mapping = {}
    for char_s, char_t in mapping.items():
        if char_t in reverse_mapping:
            return False
        reverse_mapping[char_t] = char_s

    return True

"""
💎 Exercise-3: Check Alien Dictionary
Write a function "is_alien_sorted(words: list, order: str) -> bool" that checks if words
are sorted lexicographicaly according to a new character order provided in the string order.

Example:
is_alien_sorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") -> True
"""

def is_alien_sorted(words: list, order: str) -> bool:
    pass

"""
💎 Exercise-4: Longest Substring Without Repeating Characters
Write a function "length_of_longest_substring(s: str) -> int" that takes a string s,
and returns the length of the longest substring without repeating characters.

Example:
length_of_longest_substring('abcabcbb') -> 3
"""

def length_of_longest_substring(s: str) -> int:
    charSet = set()
    l = 0
    result = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        result = max(result, r - l + 1)
    return result
"""
💎 Exercise-5: Group Shifted Strings
Write a function "group_shifted(strings: list) -> list" that takes a
list of lowercase strings and groups all strings that are generated by shifting some letters
of another string circularly. Return a list of groups, each group is a list of strings.
Groups and strings within a group can be in any order.

Example:
group_shifted(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]) -> [["abc","bcd"],["acef"],["xyz"],["az","ba"],["a","z"]]
"""

def group_shifted(strings: list) -> list:
    pass