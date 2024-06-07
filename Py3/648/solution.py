# 24.88 MB,  Beats 94.66% of users with Python3

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=len)

        def replace(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word

        words = sentence.split()

        result = [replace(word) for word in words]

        return ' '.join(result)
