my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

sum = 0
number_count = 0
for item in my_list:
    try:
        sum += item
        number_count += 1
        print('Number Count', number_count)
    except:
        continue
    finally:
        pass

else:
    print(sum)