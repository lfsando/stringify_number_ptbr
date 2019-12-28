from typing import Union, Tuple

numbers = {
    0: "",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "quatorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19: "dezenove",
    20: "vinte",
    30: "trinta",
    40: "quarenta",
    50: "cinquenta",
    60: "sessenta",
    70: "setenta",
    80: "oitenta",
    90: "noventa",
    100: "cem",
    200: "duzentos",
    300: "trezentos",
    400: "quatrocentos",
    500: "quinhentos",
    600: "seiscentos",
    700: "setecentos",
    800: "oitocentos",
    900: "novecentos",
    1000: "mil"
}


class Num2Word:
    def __init__(self, value: Union[int, float]):
        self.integer = int(value)

    def humanize(self, value=None):
        integer = self.integer if value is None else int(value)

        if numbers.get(integer): return numbers[integer]

        result = ""
        if integer < 20:
            return self.humanize_ones(integer)
        elif integer < 100:
            return self.humanize_tens(integer)
        elif integer < 1_000:
            return self.humanize_hundreds(integer)
        elif integer < 1_000_000:
            return self.humanize_thousands(integer)
        elif integer < 1_000_000_000:
            return self.humanize_millions(integer)

        return result

    def humanize_ones(self, integer: int) -> str:
        return self.validate(numbers[integer])

    def humanize_tens(self, integer: int) -> str:
        if numbers.get(integer): return numbers[integer]

        d1, d2 = [int(x) for x in str(integer)]
        return self.validate(f"{numbers[d1 * 10]} e {numbers[d2]}")

    def humanize_hundreds(self, integer: int):
        if numbers.get(integer): return numbers[integer]

        d1, d2 = self.split_number(integer, 1)
        hundreds = "cento" if d1 == 1 else numbers[d1 * 100]
        tens = self.humanize(d2)
        return self.validate(f"{hundreds} e {tens}")

    def humanize_thousands(self, integer):
        if numbers.get(integer): return numbers[integer]

        lim = 1 if integer < 10_000 else 2 if integer < 100_000 else 3
        d1, d2 = self.split_number(integer, lim)
        sep = ' e ' if (d2 <= 100 or d2 % 100 == 0) else ' '
        d1, d2 = self.humanize(d1), self.humanize(d2)
        return self.validate(f"{d1} mil {sep}{d2}")

    def humanize_millions(self, integer):
        if numbers.get(integer): return numbers[integer]

        lim = 1 if integer < 10_000_000 else 2 if integer < 100_000_000 else 3
        d1, d2 = self.split_number(integer, lim)
        million = f" milh{'ão' if d1 == 1 else 'ões'}"
        sep = ' e ' if (d2 <= 100 or d2 % 100 == 0) else ' '

        d1, d2 = self.humanize(d1), self.humanize(d2)
        d1 += million

        return self.validate(f"{d1}{sep}{d2}")

    def split_number(self, value: Union[str, int], lim: int) -> Tuple[int, int]:
        value = str(value)
        return int(value[:lim]), int(value[lim:])

    def validate(self, number: str) -> str:
        number = number.strip()
        if number.endswith(' e'):
            number = number[:-2]
        return number
