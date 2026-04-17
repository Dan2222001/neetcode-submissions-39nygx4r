class Solution:
    lengths = []
    def encode(self, strs: List[str]) -> str:
        self.lengths = []
        encoded_string = ""
        for str in strs:
            self.lengths.append(len(str))
            encoded_string = encoded_string + str
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        last_index = 0
        for length in self.lengths:
            decoded_strings.append(s[last_index:last_index + length])
            last_index += length

        return decoded_strings