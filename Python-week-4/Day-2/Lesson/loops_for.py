for i in range(5):
    print("looping through outer loop")
    for j in range(2):
        print("looping through inner loop")

for num_a in range(1,11):
    #num_a=2

    mult_table_num = ""

    for num_b in range(1,11):
        # num_b =1
        mult_table_num+= f'{num_a*num_b}'
print(mult_table_num)
