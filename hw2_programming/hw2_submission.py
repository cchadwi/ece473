
############################################################
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/ helped a lot in these problems
# Problem 1a
def lcs_length(s: str, t: str, i: int, j: int) -> int:
    """Goal: Given two text strings s[0:i] and t[0:j], return the length of their longest common subsequence.
          Implement this method using a purely recursive algorithm. (this won't be polynomial)
    Definition:
         A *subsequence* of a string s is a string that can be formed from s by deleting zero or more characters of s.
         The *longest common subsequence* of two strings s and t is the longest string that is a subsequence of both s and t.
    Example:
        "ee473" is a subsequence of "ece-47300"
    Parameters:
        s: the first string
        t: the second string
        i: an non-negative integer 0<=i<=len(s). index into the first string 
        j: an index into the second string
    Hint:
        Write an equation defining lcs_length(s,t,i,j) in terms of
        lcs_length() for just smaller values of i and j, subtracting
        one from either or both

        Your equation can condition on the comparison between the last characters of the strings.

    """

    # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
    # check if array is empty
    if i == 0 or j == 0:
        return 0
    if s[i-1] == t[j-1]:
        # If last characters of both sequences match (or X[m-1] == Y[n-1]) then 
        # L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])
        return 1 + lcs_length(s, t, i-1, j-1)
    else:
        # If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then 
        # L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]))
        return max(lcs_length(s, t, i-1, j), lcs_length(s, t, i, j-1))
    # END_YOUR_CODE


############################################################
# Problem 1b
def lcs_length_dp(s: str, t: str, i: int, j: int, table=None) -> int:
    """
    Goal: This function would implement the same goal as problem a) except this is a "memoized" version of the same function.
          To be more specific, this function would be a top-down memorized version of problem a).
    Note: You should use the provided table indexed by the pair (i, j), storing the value of LCS(s,t,i,j) if it has been computed.
          If no table is provided, create one of appropriate size for s[0:i] and t[0:j] and pass that one into recursive calls.
    """

    # BEGIN_YOUR_CODE (our solution is 10 lines of code, but don't worry if you deviate from this)
    
    '''if i == 0 or j == 0:
        return 0
    if s[i-1] == t[j-1]:
        table[i][j] = 1 + lcs_length_dp(s, t, i-1, j-1, table)
        return table[i][j]
    if table[i][j] != -1:
        return table[i][j]
    table[i][j] = max(lcs_length_dp(s, t, i, j-1, table), lcs_length_dp(s, t, i-1, j, table))
    return table[i][j]'''

    if table is None:
        table = [[-1]*(len(t)+1) for _ in range(len(s)+1)]  # use -1 to indicate empty value 
        
    if table[i][j] == -1:
        if i == 0 or j == 0:
            table[i][j] = 0
        elif s[i-1] == t[j-1]:
            table[i][j] = 1 + lcs_length_dp(s, t, i-1, j-1, table)
        else:
            table[i][j] = max(lcs_length_dp(s, t, i-1, j, table), lcs_length_dp(s, t, i, j-1, table))

    return table[i][j]

    # END_YOUR_CODE


############################################################
# Problem 1c
def lcs_length_bu(s: str, t: str, table):
    """
    Goal: Fill the provided table with subproblem lcs_length values bottom-up without recursion.
          There is no return value, this function is called for its side-effect on the table.
          It is an error for the table provided to be None.
    """

    # BEGIN_YOUR_CODE (our solution is 8 lines of code, but don't worry if you deviate from this)
    # x and y are temp variables
    for x in range(len(s)+1):
        for y in range(len(t)+1):
            if x == 0 or y == 0:
                table[x][y]=0
            elif s[x-1] == t[y-1]:
                table[x][y] = 1 + table[x-1][y-1]
            else:
                table[x][y] = max(table[x-1][y], table[x][y-1])
    # END_YOUR_CODE


############################################################
# Problem 1d
def lcs_solution_dp(s: str, t: str) -> str:
    """
    Goal: Extract the longest common subsequence between two string while utilizing top-down dp by calling your function from
          problem b).
    """
    table = [[-1]*(len(t)+1) for _ in range(len(s)+1)]

    # Table will be filled by lcs_length_dp calls that extract_soln uses to identify the choices needed
    def extract_soln(i: int, j: int):
        # BEGIN_YOUR_CODE (our solution is 8 lines of code, but don't worry if you deviate from this)
        if i == 0 or j == 0:
            return ""
        if s[i-1] == t[j-1]:
            return extract_soln(i-1, j-1) + s[i-1]
        if lcs_length_dp(s, t, i-1, j, table) >= lcs_length_dp(s, t, i, j-1, table):
            return extract_soln(i-1, j)
        else:
            return extract_soln(i, j - 1)
        # END_YOUR_CODE

    return extract_soln(len(s), len(t))


############################################################
# Problem 1e
def lcs_solution_bu(s: str, t: str) -> str:
    """
    Goal: Extract the longest common subsequence between two string while utilizing the table filling functionality in
          problem c).

    Note: solution extraction proceeds top-down even though we filled the table bottom up
    """
    table = [[-1]*(len(t)+1) for _ in range(len(s)+1)]
    lcs_length_bu(s, t, table)   # fills the table so extract_soln can just refer to table values

    def extract_soln(i: int, j: int):
        # BEGIN_YOUR_CODE (our solution is 8 lines of code, but don't worry if you deviate from this)
        if i == 0 or j == 0:
            return ""
        if s[i-1] == t[j-1]:
            return extract_soln(i-1, j-1) + s[i-1]

        if table[i-1][j] >= table[i][j-1]:
            return extract_soln(i - 1, j)
        else:
            return extract_soln(i, j - 1)
        # END_YOUR_CODE

    return extract_soln(len(s), len(t))


############################################################
# Problem 2
def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.

    Hint: Let lpl(i,j) be the longest palindrome length of the substring text[i...j].

    Argue that lpl(i,j) = lpl(i+1, j-1) + 2 if text[i] == text[j], and
                          max{lpl(i+1, j), lpl(i, j-1)} otherwise
    (be careful with the boundary cases)

    Instead of writing a recursive function to find lpl (the most
    straightforward way of implementation has exponential running time
    due to repeated computation of the same subproblems), start by
    defining a 2-dimensional array which stores lpl(i,j), and fill it
    up in the increasing order of substring length.
    """
    # BEGIN_YOUR_CODE (our solution is 13 lines of code, but don't worry if you deviate from this)
    tlen = len(text)
    if tlen == 0:
        return 0
    lpl = [[0] * tlen for _ in range(tlen)]
    for i in range(tlen):
        lpl[i][i] = 1
    # k+1 represents the substring length
    for k in range(1, tlen):
        for i in range(0, tlen-k):
            j = i + k
            if text[i] == text[j]:
                lpl[i][j] = lpl[i+1][j-1] + 2
            else:
                lpl[i][j] = max(lpl[i+1][j], lpl[i][j-1])
    return lpl[0][-1]
    
    # END_YOUR_CODE


