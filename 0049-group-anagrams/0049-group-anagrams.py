class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        for w in strs:
            key = "".join(sorted(w))
            if key not in g:
                g[key] = []
            
            g[key].append(w)

        return list(g.values())           