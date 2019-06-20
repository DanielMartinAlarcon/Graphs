import random
import sys
sys.path.insert(0, '/Users/DMA/Repos/Graphs/projects/graph')
from graph import Graph

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        if numUsers < 2:
            print('WARNING: You need at least 2 users.')
            return

        if numUsers <= avgFriendships:
            print('WARNING: The number of users must be greater than the average number of friendships.')
            return
        
        # Add users
        for i in range(numUsers):
            self.addUser(i)
        
        # Create friendships
        total_friends = 0
        while total_friends < numUsers * avgFriendships:
            # Pick a random user, give them a friend.
            lucky_user = random.randint(1, self.lastID)
            new_friend = random.choice([x for x in self.users.keys() if x != lucky_user])
            
            # If the friendship doesn't already exist, add it
            if not (new_friend in self.friendships[lucky_user] or lucky_user in self.friendships[new_friend]):
                self.addFriendship(lucky_user, new_friend)
                total_friends += 2

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """ 
        # Let's reuse our old Graph data structure
        graph = Graph()
        for user in self.users:
            graph.add_vertex(user)
        for user, friend_set in self.friendships.items():
            for friend in friend_set:
                graph.add_edge(user, friend)

        # To find the social network for one node, do a breadth-first traversal 
        # starting at that node
        social_network = sorted(graph.bft(userID))
        # The deliverable is a dictionary of the breadth-first search for each aquaintance
        # in the social network, starting at the user
        return {x:graph.bfs(userID, x) for x in social_network}


    def getSocialNetwork(self, userID):
        """
        Takes a user's userID as an argument

        Returns the social network accessible from that userID, as a list
        """ 
        # Let's reuse our old Graph data structure
        graph = Graph()
        for user in self.users:
            graph.add_vertex(user)
        for user, friend_set in self.friendships.items():
            for friend in friend_set:
                graph.add_edge(user, friend)

        # To find the social network for one node, do a breadth-first traversal 
        # starting at that node
        return sorted(graph.bft(userID))

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10,1)
    print('\nFriendships: ', sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print('Connections to 1: ', connections)
