from queue import PriorityQueue

def shortest_path(graph, start_point, target):
    
    path = PriorityQueue()
    #path[start_point] = 0
    path.put(start_point, 0)
    previous = {start_point: None}
    points = {start_point: 0}

    while not path.empty():
        current_point = path.get()

        if current_point == target:
            GenerateRoute(previous, start_point, target)

        for value in graph.roads[current_point]:
            updateScore = points[current_point] + H_Measure(graph.intersections[current_point], graph.intersections[value])
            
            if value not in points or updateScore < points[value]:
                points[value] = updateScore
                totalScore = updateScore + H_Measure(graph.intersections[current_point], graph.intersections[value])
                path.put(value, totalScore)
                previous[value] = current_point

    return GenerateRoute(previous, start_point, target)


def H_Measure(start_point, target):
    return (((start_point[0] - target[0]) ** 2) + ((start_point[1] - target[1]) ** 2))**(0.5)

def GenerateRoute(previous, start_point, target):
    current_point = target
    path = [current_point]
    while current_point != start_point:
        current_point = previous[current_point]
        path.append(current_point)
    path.reverse()
    return path
