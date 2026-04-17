class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack = []
        final = set()
        f = '('
        k = ')'
        ex_close = 0
        ex_open = 0
       
        for i in range(len(s)):
            if s[i] == f:
                stack.append(f)
            elif s[i] == k:
                if stack:
                    stack.pop()
                else:
                    ex_close += 1
        ex_open = len(stack)
        is_deleted = [False] * len(s)

        def validate():
            res = []
            stack = []
            for i in range(len(s)):
                if is_deleted[i] == False:
                    res.append(s[i])
                    if s[i] == f:
                        stack.append(i)
                    elif s[i] == k:
                        if stack:
                            stack.pop()
                        else:
                            return False
            if stack:
                return False
            else:
                final.add(''.join(res))
                return True
            
        def backtrack(i,prev_close,prev_open,path):
            if i == len(s):
                n = validate()
                return
            if s[i] == f:
                if prev_open < ex_open:
                    is_deleted[i] = True
                    backtrack(i+1,prev_close,prev_open + 1,path)
                    is_deleted[i] = False
            elif s[i] == k:
                if prev_close < ex_close:
                    is_deleted[i] = True
                    backtrack(i+1,prev_close + 1,prev_open ,path)
                    is_deleted[i] = False
            
            backtrack(i+1,prev_close,prev_open,path)

        backtrack(0,0,0,[])
        return list(final)