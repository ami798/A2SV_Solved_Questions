class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        curr=0
        ans=[]
        target=Counter(p)
        window=Counter(s[:len(p)])
        if target == window:
            ans.append(left)

        for right in range(len(p),len(s)):

            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
            
            window[s[right]] += 1

            if target == window:
                ans.append(left)
        
        return ans

        




        

