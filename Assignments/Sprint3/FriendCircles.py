""" 
There are N students in a baking class together. Some of them are friends, while some are not friends. 
The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill, 
and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of 
students who are either direct or indirect friends.

Given a N*N matrix M representing the friend relationships between students in the class. If M[i][j] = 1, 
then the ith and jth students are direct friends with each other, otherwise not.

You need to write a function that can output the total number of friend circles among all the students.
"""

def csFriendCircles(friendships):
    queue, cnt = [0], 0 # [0] represents the first individual title has been given at least one person, cnt record number of friends
    visited = [0] * len(friendships) # 0 means not visited, 1 = it had visited before
    visited[0] = 1
    
    while len(queue): # queue is not empty
        i = queue.pop() # the team A man
        for j in range(len(friendships[i])):
            if visited[j] or i == j or friendships[i][j] == 0: # visited, or their own, or is not friendship, not added
                continue
            queue.append(j) # Add into team
            visited[j] = 1 # person visited
        
        if not len(queue): # queue is empty
            cnt += 1 
            if sum(visited) < len(visited): # how others have not been assigned to friends' circle
                idx = visited.index(0) # continue into the team A man
                queue.append(idx)
                visited[idx] = 1
    return cnt

 # CSPT16/Artem Solution
def csFriendCircles(friendships):
    # for each person in the class
    # figure out what friend group they are part of
    # keep track of all people you have seen in a visited set
    # this set will be empty at first
    # for each person (0 -> N)
        # Traverse their friends
            # (dft, bft)
        # once you have completed the traversa,
        # you have found a new friend group
        # add 1 to some counter