import numpy as np

choice = 8

if choice == 1:
    m1 = np.eye(5).reshape(5, -1)
    print("EYE : ", m1)
    m1 = m1 + 5
    print("M1: ", m1)
    m2 = np.random.randint(1, 10, 5).reshape(5, -1)
    print("M2: ", m2)
    print(np.matmul(m1, m2))

    d1 = np.random.randint(3, 4, 9).reshape(3, -1)
    d2 = np.random.randint(2, 3, 9).reshape(3, -1)

    result = np.multiply(d1, d2)
    print(f"m1 element wise multiplication:{d1} with m2: {d2} and Result :{result}")

# cumulative sum
elif choice == 2:
    arr = np.random.randint(1, 1001, 1000)
    cum_sum = np.cumsum(arr)
    print(cum_sum[9], cum_sum[99], cum_sum[499])
elif choice == 3:
    # minarg and max arg:
    mat1 = np.random.randint(1, 101, 100)
    mat1 = mat1.reshape(10, -1)
    minimum = mat1.min()
elif choice == 4:
    # minimum_element_index = mat1.argmin()
    minimum_element_index = np.unravel_index(mat1.argmin(), mat1.shape)
    maximum = mat1.max()
    # maximum_element_index = mat1.argmax()
    maximum_element_index = np.unravel_index(mat1.argmax(), mat1.shape)

    print(mat1)
    print(minimum, minimum_element_index, maximum, maximum_element_index)

elif choice == 5:
    nums = np.random.rand(25)
    nums = nums.reshape(5, -1)
    r, c = np.unravel_index(np.argmax(nums), nums.shape)
    new_nums = nums.copy()
    new_nums[r][c] = 0
    print("max index is:", r, c)
    print("Original matrix", nums)
    print("Modified matrix", new_nums)
elif choice==6:
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = A[1:3, 0:2]
    B[0, 0] = 100
    print(A)
elif choice==7:
    nums1=np.random.randint(1,101,20)
    evens=[ele for ele in nums1 if ele %2==0]
    # odd_count=len(nums1-even_count)
    print(len(evens),len(nums1)-len(evens))
    #Alternate method
    even_ct=(nums1%2==0).sum()
    print(even_ct)
elif choice==8:
    nums=np.zeros(64).reshape(8,-1)
    nums[0:1,] =1
    nums[-1:,] =1
    nums[:,0:1] =1
    nums[:,-1:] =1
    print(nums)
