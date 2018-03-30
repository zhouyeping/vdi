# -*- coding: utf-8 -*-

import copy


class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]   找到所有的路径.   现在要优化一下这个解决方案, 还是超时，要分析一下这个事件复杂度呀.
        """
        wordList = set(wordList)
        current_list = [beginWord]
        res = []
        memory = {beginWord: 1}
        self.helper(current_list, wordList, endWord, res, memory)
        length = 100000
        ans = []
        for one in res:
            length = min(len(one), length)
        for one in res:
            if len(one) == length:
                ans.append(one)
        return ans

    def helper(self, current_list, word_list, end_word, res, memory):

        last_word = current_list[-1]
        if last_word in memory:
            pos_h = memory[last_word]
            pos_c = len(current_list)
            if pos_c > pos_h:
                return
            else:
                memory[last_word] = pos_c
        else:
            memory[last_word] = len(current_list)

        if last_word == end_word:
            res.append(current_list)
            return
        next_list = self.get_next(last_word, word_list)
        for one in next_list:
            tem_current = copy.deepcopy(current_list)
            tem_left = copy.deepcopy(word_list)
            tem_current.append(one)
            tem_left.remove(one)
            self.helper(tem_current, tem_left, end_word, res, memory)

    def get_next(self, word, word_list):
        res = []
        for one in word_list:
            size = len(word)
            i = 0
            cnt = 0
            while i < size:
                if word[i] != one[i]:
                    cnt += 1
                i += 1
            if cnt == 1:
                res.append(one)
        return res











