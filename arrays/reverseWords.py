class Solution:
    def reverseWords(self, s: str) -> str:
        index = 0
        n = len(s)
        words = []
        currWord = []
        # remove leading space
        while index < n and s[index] == ' ':
            index+=1
        while index < n:
            if s[index] == " ":
                index +=1
            else:
                while index!=n and s[index]!=' ':
                    currWord.append(s[index])
                    index+=1
                index+=1
                words.append("".join(currWord))
                currWord = []
        return " ".join(words[::-1])