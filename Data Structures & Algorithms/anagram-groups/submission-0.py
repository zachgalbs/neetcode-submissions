class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        # first, go through each string and populate a list of integers for each character:
        for s in strs:
            letter_frequency = [0] * 26

            for c in s:
                letter_frequency[ord(c) - ord('a')] += 1

            my_dict[tuple(letter_frequency)].append(s)
        
        return list(my_dict.values())