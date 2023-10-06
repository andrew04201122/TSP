import os

minimum_path = []
def fun(i, mask):
    if mask == ((1 << i) | 3):
        return distance[1][i]
    if memo[i][mask] != -1:
        return memo[i][mask]
    
    res = 10**9
    for j in range(1, city_numbers+1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            current_res = fun(j, mask & (~(1 << i))) + distance[j][i]
            if current_res < res:
                res = current_res
                path[i][mask & (~(1 << i))] = j  # Save the node for the path

    memo[i][mask] = res
    return res

# Construct the TSP path
def construct_path():
    mask = (1 << (city_numbers + 1)) - 1  # All cities have been visited
    u = 1  # Starting city
    minimum_path.append(u)
    # reconstruct the path
    while mask != 3:  # Until we come back to the starting city
        print(f"u : {u}, mask {bin(mask)}")
        u = path[u][mask]
        minimum_path.append(u)
        mask = mask & (~(1 << u))

    minimum_path.append(1)     
    print(f"minimum_path : {minimum_path}")   

    
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
    
            

if __name__ == '__main__':
    info, city, city_numbers, distance = decode("./HW1.config")
    ans = 10**9    
    path = [[-1]*(1 << (city_numbers + 1)) for _ in range(city_numbers + 1)]  
    neighborhood = [[] for i in range(city_numbers+1)]
    for i in range(1,city_numbers+1):
        for j in range(len(distance[i])):
            if distance[i][j] != 0 and distance[i][j] != 10**9:
                neighborhood[i].append(j)
    
    memo = [[-1]*(1 << (city_numbers+1)) for _ in range(city_numbers+1)]
    for i in range(1, city_numbers+1):
        if fun(i, (1 << (city_numbers+1))-1) + distance[i][1] < ans:
            ans = fun(i, (1 << (city_numbers+1))-1) + distance[i][1]
            path[1][(1 << (city_numbers+1))-1] = i
            #path[a][b] = next 的意義是在說，現在處在node a，b代表還沒走的node，由a走完b裡面的node下一步走value會是最短的路徑
    print("The cost of most efficient tour = " + str(ans))

    construct_path()

    # for k in range(1,7):
    #     for i,j in enumerate(memo[k]):
    #         if j != -1 and j != 1000000000:
    #             print(bin(i), j, k)