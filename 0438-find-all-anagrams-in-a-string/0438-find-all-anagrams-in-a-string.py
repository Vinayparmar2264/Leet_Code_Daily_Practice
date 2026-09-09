class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pat = p
        txt = s
        if len(pat) > len(txt):
            return []

        # Frequency map of pattern
        freq = {}
        for ch in pat:
            freq[ch] = freq.get(ch, 0) + 1

        k = len(freq)      # Number of unique characters to match
        j = 0
        result = []

        for i in range(len(txt)):

            # Expand window
            if txt[i] in freq:
                freq[txt[i]] -= 1
                if freq[txt[i]] == 0:
                    k -= 1

            # Window size becomes equal to pattern length
            if i - j + 1 == len(pat):

                if k == 0:
                    result.append(j)

                # Shrink window
                if txt[j] in freq:
                    if freq[txt[j]] == 0:
                        k += 1
                    freq[txt[j]] += 1

                j += 1

        return result