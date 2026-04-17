class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_tracker = []
        anagram_holder = []
        for str in strs:
            char_tracker = [0] * 26
            for char in str:
                char_tracker[ord(char) - ord('a')] += 1
            if char_tracker not in letter_tracker:
                letter_tracker.append(char_tracker)
                anagram_holder.append([str])
            else:
                anagram_holder[letter_tracker.index(char_tracker)].append(str)
        return anagram_holder