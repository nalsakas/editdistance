def editdistance(word1, word2):    
    def dfs(word1, word2, i, j):
        if j == len(word2):
            return 0 # base case costs 0

        collect = []
        # pass over equal character
        # reduces number of operation to worry about
        if i != len(word1) and word1[i] == word2[j]:
            i += 1 # no cost
            j += 1 # no cost

        # insert
        # allowed to insert into empty string
        res = dfs(word1, word2, i, j + 1)
        collect.append(res + 1) # costs +1

        # delete
        if i != len(word1): 
            res = dfs(word1, word2, i + 1, j)
            collect.append(res + 1) # costs +1

        # replace
        if i != len(word1):
            res = dfs(word1, word2, i + 1, j + 1)
            collect.append(res + 1) # costs +1

        return min(collect)
    
    return dfs(word1, word2, i = 0, j = 0)

word1 = "ade"
word2 = "abc"
print(editdistance(word1, word2))