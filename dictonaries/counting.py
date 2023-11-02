from collections import Counter


def canConstruct(self, ransomNote: str, magazine: str):
    # return moje(ransomNote, magazine)
    st1, st2 = Counter(ransomNote), Counter(magazine)
    print(st1, st2)
    if st1 & st2 == st1:
        return True
    return False
if __name__ == "__main__":

    counter = Counter()

