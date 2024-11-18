import re

def main():
    def validate_rom_num(num):
        if not re.fullmatch(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", num):
            print("Error: invalid input")
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

