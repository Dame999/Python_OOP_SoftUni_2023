from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not type(float_value) == float:
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(value)):
            if i > 0 and roman_values[value[i]] > roman_values[value[i - 1]]:
                result += roman_values[value[i]] - 2 * roman_values[value[i - 1]]
            else:
                result += roman_values[value[i]]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            if not type(value) == str:
                raise ValueError
            result = int(value)

        except ValueError:
            return "wrong type"
        return cls(result)


integer = Integer.from_float(2.5)
print(integer.value)

result = Integer.from_float("2.5")
print(result)

integer2 = Integer.from_roman("XIX")
print(integer2.value)

integer3 = Integer.from_string("10")
print(integer3)

result1 = Integer.from_string(1.5)
print(result1)

