_numbers = {
    0: "zero",
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


class NumeroExtenso:
    def __init__(self, value: int):
        self.integer = int(value)

    def humanize(self, value=None):
        integer = int(self.integer) if value is None else int(value)

        try:
            return _numbers[integer]
        except KeyError:
            pass

        result = ""
        if integer < 20:
            return self.humanize_ones(integer)
        elif integer < 100:
            return self.humanize_tens(integer)
        elif integer < 1000:
            return self.humanize_hundreds(integer)
        elif integer < 1000000:
            return self.humanize_thousands(integer)

        return result

    def humanize_ones(self, integer: int):
        return _numbers[integer]

    def humanize_tens(self, integer: int):
        try:
            return _numbers[integer]
        except KeyError:
            pass
        d1, d2 = [int(x) for x in list(str(integer))]
        return f"{_numbers[d1 * 10]} e {_numbers[d2]}"

    def humanize_hundreds(self, integer: int):
        try:
            return _numbers[integer]
        except KeyError:
            pass

        d1, d2 = int(str(integer)[0]), int(str(integer)[1:])
        if d1 == 1:
            hundreds = "cento"
        else:
            hundreds = _numbers[d1 * 100]
        tens = self.humanize(d2)
        return f"{hundreds} e {tens}"

    def humanize_thousands(self, integer):
        try:
            return _numbers[integer]
        except KeyError:
            pass

        if integer < 10000:
            d1, d2 = int(str(integer)[0]), int(str(integer)[1:])
            thousands = self.humanize_ones(d1) + ' mil' if d1 > 1 else 'mil'
            hundreds = self.humanize(d2)
            return f"{thousands}{' e ' if (d2 <= 100 or d2 % 100 == 0) else ' '}{hundreds}"
        elif integer < 100000:
            d1, d2 = int(str(integer)[:2]), int(str(integer)[2:])
            ten_thousands = self.humanize_tens(d1)
            thousands = self.humanize(d2)
            return f"{ten_thousands} mil{' e ' if (d2 <= 100 or d2 % 100 == 0) else ' '}{thousands}"
        elif integer < 1000000:
            d1, d2 = int(str(integer)[:3]), int(str(integer)[3:])
            hundred_thousands = self.humanize(d1)
            if d2 == 0:
                ten_thousands = ""
            else:
                ten_thousands = self.humanize(d2)

            return f"{hundred_thousands} mil{' e ' if (d2 <= 100 or d2 % 100 == 0) else ' '}{ten_thousands}"
