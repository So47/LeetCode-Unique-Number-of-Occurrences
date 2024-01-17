from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count the occurrences of each element in the array
        occurrences_count = Counter(arr)

        # Extract the occurrences as a set to remove duplicates
        occurrences = set(occurrences_count.values())

        # Compare the length of occurrences in original counter and the set
        # If they are the same, it means all occurrences are unique
        return len(occurrences_count) == len(occurrences)


        # another solution but slower 
        # arr_counter = Counter(arr)
        # seen = set()

        # for item in arr_counter:
        #     if arr_counter[item] in seen:
        #         return False
        #     seen.add(arr_counter[item])
        # return True       

        
        
