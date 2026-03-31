class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # basic anagram procedure,
        #Make dict with dict of letters to occurences and the words corresponding 
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs: 
            count = [0]  * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()

        #(O)(M * n)
