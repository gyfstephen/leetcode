# coding=utf-8
# https://leetcode-cn.com/problems/min-stack/


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p = list()
        self.q = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.p) == 0:
            self.p.append(x)
            self.q.append(x)
        else:
            self.p.append(x)
            for i in range(len(self.q) - 1, -1, -1):
                if self.q[i] < x:
                    self.q = self.q[0: i + 1] + [x] + self.q[i + 1:]
                    break
                elif i == 0 and self.q[i] >= x:
                    self.q = [x] + self.q
            print self.p, self.q

    def pop(self):
        """
        :rtype: None
        """
        val = self.p.pop()
        self.q.remove(val)

    def top(self):
        """
        :rtype: int
        """
        val = self.p[-1]
        return val

    def getMin(self):
        """
        :rtype: int
        """
        return self.q[0]
