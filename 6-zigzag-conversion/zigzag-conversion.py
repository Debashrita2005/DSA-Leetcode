class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ""
        increment = 2 * (numRows - 1)

        for r in range(numRows):
            for i in range(r, len(s), increment):
                res += s[i]

                
                if r != 0 and r != numRows - 1:
                    diagonal = i + increment - 2 * r

                    if diagonal < len(s):
                        res += s[diagonal]

        return res