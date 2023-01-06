visited_cities = ["Amsterdam", "Kiev", "Zurich", "Prague", "Berlin", "Barcelona"]
avilable_tickets = ["Paris-Skopje", "Zurich-Amsterdam", "Prague-Zurich", "Barcelona-Berlin", "Kiev-Prague", "Skopje-Paris", "Amsterdam-Barcelona", "Berlin-Kiev", "Berlin-Amsterdam"]

starting_position = "Kiev"

travledRoute = ["Kiev"]


while len(travledRoute) < len(visited_cities):
    desination = ''
    starting_point = starting_position
    for ticket in avilable_tickets:
        start, end = ticket.split("-")
        if starting_point == start:
            travledRoute.append(end)
            break
    starting_position = end
    
print(travledRoute)