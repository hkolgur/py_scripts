"""calculate maximum product of a sub array"""

n = [1,4,1,6,-3,3,-5,2,26]
k = 4
length = len(n)
if length >= k:
    curr_product = 1
    for e in n[:k]:
        curr_product *= e
    max_product=curr_product
    for i in range(length-k):
        curr_product = ((curr_product)/n[i] )*n[i+k]
        max_product=max(curr_product,max_product)
    print(f'max product of sub arry of size {k} is :{max_product}')
else:
    print("size of sub arry is less than size of original array")
