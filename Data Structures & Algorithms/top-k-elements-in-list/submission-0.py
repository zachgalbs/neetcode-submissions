class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
    
        result = []
        
        for i in range(k):
            most_freq = (0, 0)
            for key, value in my_dict.items():
                if value > most_freq[1]:
                    most_freq = (key, value)
            result.append(most_freq[0])
            del my_dict[most_freq[0]]

        return result