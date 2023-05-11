class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        counter = {}

        for i in range(len(s) - 9):
            string = s[i:i + 10]
            if not string in counter:
                counter[string] = 1
            else:
                counter[string] += 1
                if counter[string] == 2:
                    result.append(string)

        return result
