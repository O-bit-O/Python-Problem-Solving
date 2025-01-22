f = open("Input_file.txt", "r")
outputfile = open("output.txt", "w")

file_input = f.read().split("\n")


def fix_input(file_input):
    current_location_count = 0
    location = 0

    while current_location_count < len(file_input):
        asc_value = ord(file_input[current_location_count][location])

        if (asc_value < 65 or asc_value > 90) and (asc_value < 97 or asc_value > 122):
            location += 1
        else:
            if location > 0:
                file_input[current_location_count] = file_input[current_location_count][
                    location:
                ]

            location = 0
            current_location_count += 1

    return file_input


main_input = fix_input(file_input)


def addheuristicval(main_input):
    heuristic_dict = {}
    for i in main_input:
        newline = i.split(" ")
        heuristic_dict[newline[0]] = int(newline[1])

    return heuristic_dict


heuristic = addheuristicval(main_input)


def checklowervalue(current_list, node_with_distance):
    Flag = False
    for i in current_list:
        if i[0] == node_with_distance[0] and i[1] <= node_with_distance[1]:
            Flag = True
            return Flag
    return Flag


def priorityqueuelocations(current_list):
    for i in range(len(current_list) - 1):
        for j in range(i + 1, len(current_list)):
            if current_list[i][1] < current_list[j][1]:
                temp = current_list[i]
                current_list[i] = current_list[j]
                current_list[j] = temp

    return current_list


def AstarAlgo(file_input, heuristicDict, start, end):
    priority_queue = []
    visited_node = []

    priority_queue.append([start, heuristic[start], start])

    while len(priority_queue) > 0:
        popped_node = priority_queue.pop()

        if popped_node[0] == end:
            return [popped_node[2], popped_node[1] - heuristic[popped_node[0]]]

        for i in file_input:
            temp = i.strip().split(" ")

            if temp[0] == popped_node[0]:
                for j in range(2, len(temp), 2):
                    distance = (
                        int(temp[j + 1])
                        + popped_node[1]
                        - heuristic[popped_node[0]]
                        + heuristic[temp[j]]
                    )

                    if checklowervalue(visited_node, [temp[j], distance]) == False:
                        priority_queue.append(
                            [temp[j], distance, (popped_node[2] + "->" + temp[j])]
                        )
                        visited_node.append([temp[j], distance])
                        priority_queue = priorityqueuelocations(priority_queue)

                break


beginning = input("Start location: ")
destination = input("Destination: ")


if beginning in heuristic and destination in heuristic:
    main_output = AstarAlgo(main_input, heuristic, beginning, destination)

    totaloutput = "Path: " + main_output[0] + "\n"
    totaloutput += "Total distance: " + str(main_output[1]) + "km"
    outputfile.write(totaloutput)

else:
    outputfile.write("Start or end node doesn't exist")
