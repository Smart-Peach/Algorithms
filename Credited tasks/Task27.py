class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        counter = {}

        for i in range(len(s) - 9):
            string = s[i:i + 10]
            counter[string] = counter.get(string, 0) + 1  #

            if counter[string] == 2:
                result.append(string)

        return result
