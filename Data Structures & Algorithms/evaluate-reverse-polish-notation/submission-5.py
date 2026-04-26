class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []

        for token in tokens:
            try:
                values.append(int(token))

            except:
                if token == "+":
                    second = values.pop()
                    values.append(values.pop() + second)

                elif token == "-":
                    second = values.pop()
                    values.append(values.pop() - second)

                elif token == "*":
                    second = values.pop()
                    values.append(values.pop() * second)

                elif token == "/":
                    second = values.pop()
                    values.append(int(values.pop() / second))

            
        return values[0]