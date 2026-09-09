class Solution:
    def isValid(self, s: str) -> bool:

        stk = []

        for el in s:
            if el not in [")","]","}"]:
                stk.append(el)
            elif len(stk) > 0 :
                top = stk[-1]
                if (top == "(" and el == ")") or (top == "{" and el == "}") or top == "[" and el == "]":
                    stk.pop()
                else:
                    return False
            else:
                return False

            
        return True if len(stk) == 0 else False
        