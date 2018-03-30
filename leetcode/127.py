# -*- coding: utf-8 -*-
import copy


class Solution(object):  # 还是超时.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_next = {}
        for one in wordList:
            word_next[one] = self.get_next(one, wordList)
        word_next[beginWord] = self.get_next(beginWord, wordList)
        current = [beginWord]
        memory = {
            beginWord: True
        }
        res = []
        self.helper(current, memory, res, wordList, endWord, word_next)

        length = 100000
        for one in res:
            if one[-1] != endWord:
                continue
            length = min(length, len(one))
        if length == 100000:
            return 0
        return length

    def helper(self, current, memory, res, wordList, end_word, cache):
        word = current[-1]
        if word == end_word:
            res.append(current)
            return
        word_next = cache[word]
        flag = False
        for one in word_next:
            if one not in memory:
                flag = True
                tem_memory = copy.deepcopy(memory)
                tem_current = copy.deepcopy(current)
                tem_memory[one] = True
                tem_current.append(one)
                self.helper(tem_current, tem_memory, res, wordList, end_word, cache)
        if flag is False:
            res.append(current)

    def get_next(self, word, wordList):
        res = []
        for one in wordList:
            size = len(one)
            i = 0
            cnt = 0
            while i < size:
                if one[i] != word[i]:
                    cnt += 1
                i += 1
            if cnt == 1:
                res.append(one)
        return res


class Solution2:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        queue = []
        queue.append((beginWord, 1))
        while queue:
            first = queue.pop(0)
            if first[0] == endWord:
                return first[1]

            for i in range(len(first[0])):
                word = first[0]
                for j in range(26):
                    word[i] = chr(ord('a') + j)
                    if wordList.find(word) != -1:
                        wordList.remove(word)
                        queue.append((word, first[1] + 1))

        return 0



if __name__ == '__main__':
    s = Solution()
    begin_word = 'hit'
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    end_word = 'cog'
    res = s.ladderLength(begin_word, end_word, wordList)
    for one in res:
        print one










