def solution(routes):
    answer = 0
    ptr = 0
    routes.sort()

    while routes:
        current_route = routes[0]
        start = current_route[0]
        end = current_route[1]

        routes.remove(current_route)
        tmp_routes = routes[:]
        answer += 1
        
        for route in routes:
            if not (start > route[1] or end < route[0]):
                tmp_routes.remove(route)

                if start < route[0]:
                    start = route[0]
                if end > route[1]:
                    end = route[1]
             
        routes = tmp_routes

    return answer