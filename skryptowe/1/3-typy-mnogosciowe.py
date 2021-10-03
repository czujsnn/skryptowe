list = [x for x in range(int(10))]

for elem in list:
    print(elem,end='\n')

for iter in range(len(list)):
    print(f"Tab[{iter}] = {list[iter]}")

test_dict = {"1":11,"2":22,"3":33,"4":44,"5":55,"21":37}

for k in test_dict:
    print(f"HASH[{k}] = {test_dict[k]}")


    