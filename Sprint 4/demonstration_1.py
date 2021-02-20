"""
You are given a non-empty list of words.

Write a function that returns the *k* most frequent elements.

The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.

Example 1:

```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2

Output:
["lambda", "school"]

Explanation:
"lambda" and "school" are the two most frequent words.
```

Example 2:

```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4

Output:
["the", "is", "cloudy", "sky"]

Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```

Notes:

- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""
def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int

    Output:
    List[str]
    """
    # Your code here
    # Build our frequency_dict
    word_dict = {}

    for word in words:
        if word not in word_dict:
            # Add the new word to the dictionary
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    print(word_dict)

    print(list(word_dict.items()))
    sorted_values = sorted(list(word_dict.items()), key=return_second_item, reverse=True)

    return [x[0] for x in sorted_values[0:k]]

def return_second_item(item):
    return item[1]

(top_k_frequent(["rules", "lambda", "school", "lambda", "school", "rocks"], 2))
