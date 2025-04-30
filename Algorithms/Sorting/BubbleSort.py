my_arr = [5, 3, 8, 4, 2]

for i in range(1, len(my_arr)):
    pointer = 0
    print(f"Pass: {i}")
    for j in range(1, len(my_arr)):
        if my_arr[pointer] > my_arr[pointer + 1]:
            my_arr[pointer], my_arr[pointer + 1] = my_arr[pointer + 1], my_arr[pointer]
        print(my_arr)
        pointer += 1
