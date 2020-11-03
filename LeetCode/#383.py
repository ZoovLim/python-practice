class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if magazine.find(c) == -1:
                return False
            magazine = magazine.replace(c, 'A', 1)
        return True
