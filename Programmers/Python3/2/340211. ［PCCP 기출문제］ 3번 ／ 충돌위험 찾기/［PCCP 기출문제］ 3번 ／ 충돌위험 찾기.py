from collections import Counter

def solution(points, routes):
    point_dict = {}

    for i in range(len(points)):
        point_dict[i + 1] = points[i]
    
    all_robot_paths = []
    max_time = 0
    
    robot_history = []
    for route in routes:
        path = []
        curr_r, curr_c = point_dict[route[0]]
        path.append((curr_r, curr_c))
        
        for i in range(1, len(route)):
            next_r, next_c = point_dict[route[i]]
            
            while curr_r != next_r:
                if curr_r < next_r:
                    curr_r += 1
                else:
                    curr_r -= 1
                path.append((curr_r, curr_c))
                
            while curr_c != next_c:
                if curr_c < next_c:
                    curr_c += 1
                else:
                    curr_c -= 1
                path.append((curr_r, curr_c))
        
        robot_history.append(path)
        max_time = max(max_time, len(path))
    
    total_collisions = 0
    for t in range(max_time):
        positions_at_t = []
        for path in robot_history:
            if t < len(path):
                positions_at_t.append(path[t])
        
        count = Counter(positions_at_t)
        for pos in count:
            if count[pos] >= 2:
                total_collisions += 1
                
    return total_collisions