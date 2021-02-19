class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        output = []
        
        def build_all_combos_for_num(current_i, given_str=''):
            num = digits[current_i]
            for letter in key_map[num]:
                new_str = given_str + letter
                # if no more numbers, we know this is the longest string
                if current_i == len(digits) - 1:
                    output.append(new_str)
                else:
                    # We havent finished building this string
                    build_all_combos_for_num(current_i + 1, new_str)
        
        if (len(digits) > 0):
            build_all_combos_for_num(0, '')
        
        return output
