class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        from collections import defaultdict

        if not list1 or not list2:
            return []

        common = defaultdict(lambda : [])
        list_dict = {v:i for i,v in enumerate(list1)}

        for index, r in enumerate(list2):
            if r in ld:
                common[index + ld[r]].append(r)
                
        val = min(common.keys())

        return common[val]
	