import collections
import math
import numpy as np

## Note: these are for historical reasons called problem 3a-g but are assigned as problem 1
############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max(text.split())
    # END_YOUR_CODE

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt(sum((loc1[i] - loc2[i])**2 for i in [0,1]))
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the original sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 21 lines of code, but don't worry if you deviate from this)
    
    # using the example code to try to figure out how to do this
    # create a function inside the function that uses adjacency list to return the length n of the sentences 
    def adj_search(adj, head, n):
        if n == 1:
            return {head} # makes head a set
        out = set() # makes out a set, not a list
        for nxt in adj[head]:
            nxt_sentence = adj_search(adj, nxt, n-1) # finds next setence to compare
            for ns in nxt_sentence:
                out.add(head + ' ' + ns)
        return out
            
    # using the new function create the list of similar sentences 
    word = sentence.split()
    n = len(word)
    if n == 0:
        return
    # Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. 
    # The functionality of both dictionaries and defaultdict are almost same except for the fact 
    # that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
    adj = collections.defaultdict(set)
    for i in range(n-1):
        adj[word[i]].add(word[i+1]) # adding the next word to the list
    if word[-1] not in adj:
        adj[word[-1]] = set() # takes out the non similar words
    out = list()
    for head in adj.keys(): # keys returns a view object
        out.extend(adj_search(adj, head, n))
    return out
    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2): 
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return sum(v1[i]*v2[i] for i in v1.keys() & v2.keys()) # gets the keys of v1 and v2 and multiplies them. basically dot product calculation
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for i in v2:
        v1[i] = v1.get(i,0) + scale * v2[i] # The get() method returns the value of the item with the specified key.
    # END_YOUR_CODE

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    word_counter = collections.defaultdict(int)
    for w in text.split():
        word_counter[w] +=1
    return {w for w in word_counter if word_counter[w] == 1}
    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.

    Hint: Let lpl(i,j) be the longest palindrome length of the substring text[i...j].

    Argue that lpl(i,j) = lpl(i+1, j-1) + 2 if text[i] == text[j], and
                          max{lpl(i+1, j), lpl(i, j-1)} otherwise
    (be careful with the boundary cases)


    FOR HOMEWORK 1, you may write a recursive version as described above.
    FOR HOMEWORK 2, you will have to write the non-recursive version described next, 
    which you can go ahead and do now if you understand how:
    
    Instead of writing a recursive function to find lpl (the most
    straightforward way of implementation has exponential running time
    due to repeated computation of the same subproblems), start by
    defining a 2-dimensional array which stores lpl(i,j), and fill it
    up in the increasing order of substring length.
    """
    # BEGIN_YOUR_CODE (our non-recursive solution is 13 lines of code, but don't worry if you deviate from this)
    def LongestSubLength(i,j):
        if i == j:
            return 1
        elif i > j:
            return 0
        elif text[i] == text[j]:
            return LongestSubLength(i+1, j-1) + 2
        else:
            return max(LongestSubLength(i+1, j), LongestSubLength(i, j-1))

    n = len(text)
    if n <= 1:
        return n
    maxlen = LongestSubLength(0, len(text) - 1)
    return maxlen
    # END_YOUR_CODE
