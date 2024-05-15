# a = [10,13,17,20]
# print(a)

# #リストのメソッド追加
# nums = [1,2,3]
# print(nums)
# nums.append(4) #リストの末尾に4を追加
# print(nums)
# nums.extend([5,6,7])#リストの末尾に異なるリスト([5,6,7])を追加
# print(nums)
# nums

# #特定の要素を削除
# nums = [0,1,2,3,4]
# del nums[2]
# print(nums)
# nums = [0,1,2,3,4]
# del nums[2:4]
# print(nums)

#辞書型
ages = {'鈴木':30, '井上':20, '伊藤':21}
print(ages['伊藤'])
print('井上' in ages)
print(ages.values())
print(list(ages.keys())[2])