class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}

        for w in strs:
            k = "".join(sorted(w))
            if k not in g:
                g[k] = []

            g[k].append(w)

        return list(g.values())

            