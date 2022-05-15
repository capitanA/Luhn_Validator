class ModuleTen:
    def __init__(self, input=str, checkdigitpos=int(5)):
        self.input = input
        self.checkdigitpos = checkdigitpos

    def get_weight(self, digit_pos):
        if (len(self.input) % 2 == 0) ^ (digit_pos % 2 == 0):
            return 1

        return 2

    def digit_multiply_by_weight(self, digit_pos, digit_value):
        production = digit_value * self.get_weight(digit_pos)
        return (production // 10) + (production % 10)

    def splitter(self):
        index = self.checkdigitpos - 1
        input_checkdigit_excluded = self.input[0: index:] + self.input[index + 1::]
        checkdigit = self.input[self.checkdigitpos - 1]

        return input_checkdigit_excluded, int(checkdigit)

    def validate(self):
        input_checkdigit_excluded, checkdigit = self.splitter()
        weighted_list = [self.digit_multiply_by_weight(digit_pos, int(digit_value)) for (digit_pos, digit_value) in
                         enumerate(str(input_checkdigit_excluded))]

        # check if the Module10 algorithm calculated the same checkdigit as the one in the PHN!
        return 10 - (sum(weighted_list) % 10) == checkdigit