class Solution:
    def toLowerCase(self, s: str) -> str:
        r=''
        for char in s:
            if 65<=ord(char)<=90:
                r+=chr(ord(char)+32)
            else:
                r+=char
        return r      