num=int(input("Enter the number of tuples:"))
tup_list=[]
for i in range(num):
    elements=input(f"Enter the elements of the tuple{i+1}")
    tuple_elements=tuple(map(int,elements.split()))
    tup_list.append(tuple_elements)
result=list(map(sum,tup_list))
print("sum of elements in each tuple:",result)
