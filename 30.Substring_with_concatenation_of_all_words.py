# 504ms, faster 45.17%
# 12.9MB, less than 100%

class Solution:
    def findSubstring(self, s:str, words: List[str]) -> List[int]:
        word_num = len(words)
        str_len = len(s)
        if word_num == 0 or str_len == 0:
            return []
        word_len = len(words[0])
        out = []
        word_dict = {}
        for word in words:
            word_dict[word] = 1 if word not in word_dict else word_dict[word]+1

        for i in range(word_len):
            count = 0
            d = {key:0 for key in word_dict}
            left, right = i, i
            while right <= str_len-word_len:
                if s[right:right+word_len] in d:
                    if d[s[right:right+word_len]] < word_dict[s[right:right+word_len]]:
                        d[s[right:right+word_len]] += 1
                        count += 1
                        right += word_len
                        if count == word_num:
                            out.append(left)
                            d[s[left:left+word_len]] -= 1
                            left += word_len
                            count -= 1
                    else:
                        d[s[left:left+word_len]] -= 1
                        left += word_len
                        count -= 1
                else:
                    d = {key:0 for key in word_dict}
                    right += word_len
                    left = right
                    count = 0
        return out