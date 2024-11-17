import re

def main():
    def parse_rom_num(num):
        dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        i = 0

        while i < len(num):
            if i != len(num) - 1 and dict[num[i]] < dict[num[i+1]]:
                total += dict[num[i+1]] - dict[num[i]]
                i += 2
            else:
                total += dict[num[i]]
                i += 1

        return total

    while True:
        numeral = input("Insert a roman numeral number ('q' to quit): ")
        if numeral:
            numeral = numeral.upper()

        if numeral == "Q":
            break
        if re.search("[^MDCLXVImdclxvi]", numeral):
            print("Error: The expression contains characters that are not allowed")
        elif re.search("M{4}|D{2}|C{4}|L{2}|X{4}|V{2}|I{4}", numeral):
            print("Error: Roman numerals that are powers of 10 cannot appear more than 3 times; roman numerals that are multiples of 5 but not multiples of 10 cannot appear more than once")
        elif (numeral.count("CM") > 1 or numeral.count("CD") > 1 or (re.search("(CM|CD)(?=C|D)", numeral)) or
            numeral.count("XC") > 1 or numeral.count("XL") > 1 or (re.search("(XC|XL)(?=X|L)", numeral)) or
            numeral.count("IX") > 1 or numeral.count("IV") > 1 or (re.search("(IX|IV)(?!$)", numeral))):
            print("Error: unexpected token after subtractive operation token")
        elif re.search("I(?!$|X$|V$|I$|II$)|IIX|IIV", numeral):
            print("Error: unexpected token after token 'I'")
        elif re.search("V(?!$|I)", numeral):
            print("Error: unexpected token after token 'V'")
        elif re.search("X(?!$|C|L|X|V|I)|XXC|XXL", numeral):
            print("Error: unexpected token after token 'X'")
        elif re.search("L(?!$|X|V|I)", numeral):
            print("Error: unexpected token after token 'L'")
        elif re.search("C(?!$|M|D|C|L|X|V|I)|CCM|CCD", numeral):
            print("Error: unexpected token after token 'C'")
        elif re.search("D(?!$|C|L|X|V|I)", numeral):
            print("Error: unexpected token after token 'D'")
        elif re.search("M(?!$|M|D|C|L|X|V|I)", numeral):
            print("Error: unexpected token after token 'M'")
        else:
            print(f"{numeral} is equal to {parse_rom_num(numeral)}")

if __name__ == "__main__":
    main()

