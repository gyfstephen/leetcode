# coding=utf-8
# https://leetcode-cn.com/problems/string-to-integer-atoi/


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        valid = False
        ans = list()
        for i in str:
            if i == ' ' and not ans and valid is False:
                continue
            elif i == ' ' and ans and valid is True:
                break
            elif i == ' ' and ans and valid is False:
                return 0
            elif i in ['-', '+'] and ans and valid is False:
                return 0
            elif i in ['-', '+'] and ans and valid is True:
                break
            elif i in ['-', '+'] and not ans:
                ans.append(i)
            elif i.isalpha() and not ans:
                return 0
            elif i.isalpha() and ans and valid is False:
                return 0
            elif i.isalpha() and ans and valid is True:
                break
            elif i.isdigit() and not ans:
                ans.append(i)
                valid = True
            elif i.isdigit() and ans and valid is False:
                ans.append(i)
                valid = True
            elif i.isdigit() and ans and valid is True:
                ans.append(i)
            elif ans and valid is True:
                break
            elif ans and valid is False:
                return 0
            elif not ans:
                return 0
        if valid is True:
            ans = int(''.join(ans))
            if ans > 2147483647:
                return 2147483647
            elif ans < -2147483648:
                return -2147483648
            else:
                return ans
        else:
            return 0
