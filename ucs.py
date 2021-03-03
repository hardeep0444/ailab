def  uniform_cost_search(goal, start):

    global graph,cost



    visited = {}

    queue = []

    queue.append([0, start])

 

    while (len(queue) > 0):

        queue = sorted(queue)

        p = queue[-1]

        del queue[-1]

 

        p[0] *= -1



        if (p[1] == goal):

            return p[0]



        if (p[1] not in visited):

            for i in range(len(graph[p[1]])):

                queue.append( [ ( p[0] + cost[ (p[1], graph[p[1]][i]) ] ) * -1, graph[ p[1] ][ i ] ] )



        visited[p[1]] = 1

 

graph,cost = [[] for i in range(8)],{}



graph[0].append(1)

graph[0].append(2)

graph[1].append(4)

graph[2].append(1)

graph[2].append(3)

graph[3].append(7)

graph[4].append(3)

graph[4].append(5)

graph[4].append(6)



cost[(0, 1)] = 7

cost[(0, 2)] = 3

cost[(1, 4)] = 6

cost[(2, 1)] = 2

cost[(2, 3)] = 9

cost[(3, 7)] = 13

cost[(4, 5)] = 2

cost[(4, 6)] = 1

cost[(4, 3)] = 3



goal = 3



answer = uniform_cost_search(goal, 0)



print("Minimum cost from 0 to {0} is = {1}".format(goal, answer))
