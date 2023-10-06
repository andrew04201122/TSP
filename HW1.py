import os
minimum_path = []
def fun(i, mask):
	# base case
	# if only ith bit and 1st bit is set in our mask,
	# it implies we have visited all other nodes already
	if mask == ((1 << i) | 3):
		return distance[1][i]

	# memoization
	if memo[i][mask] != -1:
		return memo[i][mask]

	res = 10**9 # result of this sub-problem

	# we have to travel all nodes j in mask and end the path at ith node
	# so for every node j in mask, recursively calculate cost of
	# travelling all nodes in mask
	# except i and then travel back from node j to node i taking
	# the shortest path take the minimum of all possible j nodes
	for j in range(1, city_numbers+1):
		if (mask & (1 << j)) != 0 and j != i and j != 1:
			res = min(res, fun(j, mask & (~(1 << i))) + distance[j][i])
	memo[i][mask] = res # storing the minimum value
	return res

def decode(config):
    fp_read = open(config, 'r')
    info = []
    city = set()
    for i, eachline in enumerate(fp_read.readlines()):
        info.append(eachline.rstrip('\n').split())
        info[i][1] = int(info[i][1])
        city.add(info[i][2])
        city.add(info[i][3])
    fp_read.close()
    
    global city_numbers
    global distance
    city_numbers = len(city)
    distance = [[10**9 for _ in range(city_numbers+1)] for _ in range(city_numbers+1)]
    distance[0] = [0 for _ in range(city_numbers+1)]
    for i in range(1, city_numbers+1):
        distance[i][0] = 0
        for j in range(1, city_numbers+1):
            if i == j:
                distance[i][j] = 0
            else:
                for edge in info:
                    if (edge[2] == 'v{}'.format(i) and edge[3] == 'v{}'.format(j)) or edge[3] == 'v{}'.format(i) and edge[2] == 'v{}'.format(j):
                    #if (edge[2] == i and edge[3] == j) or (edge[3] == i and edge[2] == j):
                        distance[i][j] = edge[1]
    return info, city, city_numbers, distance


# Driver program to test above logic
if __name__ == '__main__':
    info, city, city_numbers, distance = decode("./HW1.config")
    ans = 10**9
    # memoization for top down recursion
    memo = [[-1]*(1 << (city_numbers+1)) for _ in range(city_numbers+1)]
    
    for i in range(1, city_numbers+1):
	# try to go from node 1 visiting all nodes in between to i
	# then return from i taking the shortest route to 1
        ans = min(ans, fun(i, (1 << (city_numbers+1))-1) + distance[i][1])

    print("The cost of most efficient tour = " + str(ans))
