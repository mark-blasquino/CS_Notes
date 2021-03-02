""" 
You've uncovered a secret alien language. To your surprise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order of the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically"(based on the supplied alphabet), will determine if the given words
are sorted "alphabetically" in this secret language.

Example 1:

Input words = ["lambda", "school"], order = "hlabcdefghijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.

Example 3:

Input: words = ["lambda", "lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size). According to lexicographical rules "lambda" > "lamb",
because 'd' > 'theta', where 'theta' is defined as the blank character which is less
than any other character

Understand
    input:  array of words
            order of characters as a string
    output: boolean

Plan
    for two words A, B:
        - check all letters of both words
            - see which letter comes first
            if letter of second word comes before first word
                not in order
        if done checking letters
            if a is longer return false
"""

def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    # prebuild a dictionary
    lookup_dict = {}
    for i in range(len(alpha_order)):
        lookup_dict[alpha_order[i]] = i

    # for all words
    # for each word (A), compare it to its neighbor (B)
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        # check all letters of both words (A, B)
        for char_i in range(min(len(word1), len(word2))):
            # how do we actually compare the letters?
            # if any letter in B comes before A, we know it's not in order
            if word1[char_i] != word2[char_i]:
                # if the letters are different check that letter2 comes after letter1
                if lookup_dict[word1[char_i]] > lookup_dict[word2[char_i]]:
                    return False
                # else, break out of this loop
                break

        # if A is longer than B, it's also not in order
        if len(word1) > len(word2):
            return False

    return True

print(are_words_sorted(['lambda', 'school'], 'hlabcdefghijkmnopqrstuvwxyz'))
print(are_words_sorted(["lambda", "lamb"], 'abcdefghijklmnopqrstuvwxyz'))