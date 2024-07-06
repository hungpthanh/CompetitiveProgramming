class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "($)"
        results = "($)".join(strs)
        return results

    def decode(self, s: str) -> List[str]:
        if s == "($)":
            return []
        results = s.split("($)")
        return results
