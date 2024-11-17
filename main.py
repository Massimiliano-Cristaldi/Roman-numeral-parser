import re

def main():
    def validate_rom_num(num):
        if re.search("[^MDCLXVImdclxvi]", num):
            print("Error: The expression contains characters that are not allowed")
            return False
        elif re.search("M{4}|D{2}|C{4}|L{2}|X{4}|V{2}|I{4}", num):
            print("Error: Roman numerals that are powers of 10 cannot appear more than 3 times; roman numerals that are multiples of 5 but not multiples of 10 cannot appear more than once")
            return False
        elif (num.count("CM") > 1 or num.count("CD") > 1 or (re.search("(CM|CD)(?=C|D)", num)) or
            num.count("XC") > 1 or num.count("XL") > 1 or (re.search("(XC|XL)(?=X|L)", num)) or
            num.count("IX") > 1 or num.count("IV") > 1 or (re.search("(IX|IV)(?!$)", num))):
            print("Error: unexpected token after subtractive operation token")
            return False
        elif re.search("I(?!$|X$|V$|I$|II$)|IIX|IIV", num):
            print("Error: unexpected token after token 'I'")
            return False
        elif re.search("V(?!$|I)", num):
            print("Error: unexpected token after token 'V'")
            return False
        elif re.search("X(?!$|C|L|X|V|I)|XXC|XXL", num):
            print("Error: unexpected token after token 'X'")
            return False
        elif re.search("L(?!$|X|V|I)", num):
            print("Error: unexpected token after token 'L'")
            return False
        elif re.search("C(?!$|M|D|C|L|X|V|I)|CCM|CCD", num):
            print("Error: unexpected token after token 'C'")
            return False
        elif re.search("D(?!$|C|L|X|V|I)", num):
            print("Error: unexpected token after token 'D'")
            return False
        elif re.search("M(?!$|M|D|C|L|X|V|I)", num):
            print("Error: unexpected token after token 'M'")
            return False
        else:
            return True

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

    str_validated = False

    while str_validated == False:
        numeral = input("Insert a roman numeral number ('q' to quit): ")
        if numeral:
            numeral = numeral.upper()

        if numeral == "Q":
            return
        str_validated = validate_rom_num(numeral)

    if str_validated:
        result = parse_rom_num(numeral)
        print(f"{numeral} is equal to {result}")

if __name__ == "__main__":
    main()

