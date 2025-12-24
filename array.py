import random

# 初始化数组
arr: list[int] = [0] * 5
nums: list[int] = [1,3,2,5,4] 

print('arr:', arr)
print('nums:',nums)

# 随机访问元素
def random_access(nums:list[int]):
    '''随机访问元素'''
    # 在区间访问[0, len(nums)-1]中随机抽取一个数字
    random_index = random.randint(0,len(nums)-1)
    print('index:',random_index)
    # 获取并返回随机元素
    random_num = nums[random_index]
    return random_num


print('num:',random_access(nums))

# 插入元素
def insert(nums:list[int],num:int,index:int):
    '''在数组的索引index处插入数字num'''
    # 把索引index以及以后的所有元素都向后移动一位，最后一位丢失
    for i in range(len(nums)-1,index,-1):
        nums[i] = nums[i-1]
    nums[index] = num
    
insert(arr,2,3)
print('arr',arr)

## 数组的长度是不可变的，存储在连续的内存空间里