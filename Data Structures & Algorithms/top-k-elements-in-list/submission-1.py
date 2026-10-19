class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_of_nums = {}

        for el in nums:
            if el not in dict_of_nums.keys():
                dict_of_nums[el] = 1
            else:
                dict_of_nums[el] += 1

        dict_of_nums = dict(sorted(dict_of_nums.items(), key=lambda x: x[1], reverse=True))

        list_of_nums = []

        for i in range(k):
            list_of_nums.append(list(dict_of_nums.keys())[i])

        return list_of_nums
        