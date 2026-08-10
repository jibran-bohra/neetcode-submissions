class Solution:
    def __init__(self):
        self.delimiter = "?"

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string += str(len(s)) + self.delimiter + s
        
        return string

    def decode(self, s: str) -> List[str]:
        array = []
        i = 0

        while i < len(s):
            length = ""

            while s[i] != self.delimiter:
                length += s[i]
                i += 1

            length = int(length)
            i += 1

            # Read the string of the given length
            array.append(s[i:i + length])

            # Move to the start of the next encoded string
            i += length

        return array