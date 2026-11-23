class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bag = dict()
        for i in strs:
            keyValue = "".join(sorted(i))
            valueList = bag.get(keyValue, [])
            valueList.append(i)
            bag[keyValue] = valueList

        return [i for i in bag.values()]