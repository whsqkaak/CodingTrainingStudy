def solution(tickets):
    paths = find_path("ICN", tickets, ["ICN"])
    paths = list(filter(lambda x: type(x) != str, paths))
    answer_path = paths[0]
    
    for path in paths[1:]:
        answer_path = compare_paths(answer_path, path)
    return answer_path

def find_path(start_port, tickets, result):
    possible_tickets = list(filter(lambda ticket:start_port == ticket[0], tickets))
    
    if possible_tickets == []:
        return result

    paths = []
    for ticket in possible_tickets:
        tickets_copy = tickets.copy()
        tickets_copy.remove(ticket)

        new_path = find_path(ticket[1], tickets_copy, result + [ticket[1]])

        if len(new_path) == len(tickets) + len(result):
            paths.append(new_path)
        else:
            for tmp in new_path:
                paths.append(tmp)

    return paths

def compare_paths(path_1, path_2):
    zip_path = zip(path_1, path_2)
    for ports in zip_path:
        if ports[0] > ports[1]:
            return path_2
        elif ports[0] < ports[1]:
            return path_1
    
    return path_1

if __name__ == "__main__":
    tickets = [["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]]
    print(solution(tickets))