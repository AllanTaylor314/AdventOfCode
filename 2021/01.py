with open('01.txt') as file:
    data=file.read().splitlines()

nums = list(map(int,data))
print('Part 1:',len([a for a,b in zip(nums,nums[1:]) if a<b]))

sums=list(map(sum,zip(nums,nums[1:],nums[2:])))
print('Part 2:',len([a for a,b in zip(sums,sums[1:]) if a<b]))