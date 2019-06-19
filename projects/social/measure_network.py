from social import SocialGraph
import numpy as np
# for _ in range(10):

sg = SocialGraph()
sg.populateGraph(200,5)

network_size = np.mean([len(sg.getSocialNetwork(x)) for x in sg.users.keys()])
print('Average size of social network: ', network_size)


all_users = [x for x in sg.users.keys()]
path_dicts = [sg.getAllSocialPaths(user) for user in all_users]
ex_dict = path_dicts[0]
average_separation = np.mean([np.mean([len(path) for user, path in path_dict.items()]) for path_dict in path_dicts])
print('Average distance to the neighbors: ', average_separation)
# print(np.mean([len(sg.getAllSocialPaths(x)) ))