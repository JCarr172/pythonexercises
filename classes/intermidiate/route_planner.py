def route_planner(input):
    print(input)
    route = [sorted(input)[0]]

    while route[-1] != 15:
        difference = []
        for i in range(1,len(input)):
            difference.append(input[i]-route[-1])
        
        index_ = sorted(difference)[0]
        print(input.index(index_))
        route.append(sorted(difference)[0])
        print(difference)
        print(route)


route_planner([0,8,4,12,2,10,6,14,1,9,5,12,3,11,7,15])