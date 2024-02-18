def selection_sort(input_list):

    n = len(input_list)

    for i in range(0,n):
        minimum = i

        for j in range(i+1,n):
            if input_list[j] < input_list[minimum]:
                minimum = j

        input_list[i], input_list[minimum] = input_list[minimum], input_list[i]
    return input_list

input_list = [9,2,1,44,2,1]

print(selection_sort(input_list))