'''
https://leetcode.com/problems/solve-the-equation/
Input: "x+5-3+x=6+x-2"
Output: "x=2"

Input: "x=x"
Output: "Infinite solutions"
'''


class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.replace('"', '')
        flip_sign = lambda s: '+' if s == '-' else '-'
        lhs, rhs = equation.split('=')
        updated_rhs = "".join([c if c not in ('+', '-') else flip_sign(c) for c in rhs])
        if updated_rhs[0] not in ['+', '-']:
            updated_rhs = '-' + updated_rhs

        updated_equation_lhs = lhs + updated_rhs
        if not updated_equation_lhs[0] in ['+', '-']:
            updated_equation_lhs = '+' + updated_equation_lhs

        plus_minus_pos = [i for i, x in enumerate(updated_equation_lhs) if x in ('+', '-')]
        x_parts = []
        number_parts = []

        def add_data(data):
            if 'x' in data:
                x_parts.append(data)
            else:
                number_parts.append(data)

        previous_pos = 0
        for i in plus_minus_pos[1:]:
            data = updated_equation_lhs[previous_pos:i]
            previous_pos = i
            add_data(data)
        # Adding the last part of equation that is missing in the above loop
        add_data(updated_equation_lhs[plus_minus_pos[-1]:])

        get_int_part = lambda x: int(x[:-1]) if len(x) > 2 else int(x[0] + '1')
        sum_of_number_parts = sum([int(x) for x in number_parts])
        sum_of_x_parts = sum([get_int_part(x) for x in x_parts])

        if sum_of_x_parts == 0 and sum_of_number_parts == 0:
            return 'Infinite solutions'
        elif sum_of_x_parts == 0 and sum_of_number_parts != 0:
            return 'No solution'
        x_value = int(-sum_of_number_parts / sum_of_x_parts)
        return 'x=' + str(x_value)


s = Solution()
print(s.solveEquation(input('Enter the equation :')))
