class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            
            if tuple(freq) in ans:
                ans[tuple(freq)].append(word)
            else:
                ans[tuple(freq)] = [word]
        
        return list(ans.values())



        