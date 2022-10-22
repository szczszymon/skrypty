# -*- coding: utf-8 -*-
import re


def Find(txt):
    return [re.findall('\d+', txt), re.findall('[A-Ząćółńżźśę]+', txt, re.IGNORECASE)]


if __name__ == "__main__":
    while True:
        try:
            text = input('Wprowadź tekst: ')

            res = Find(text)

            nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            int_ctr = chr_ctr = 0
            prev = ""

            for char in text:

                match prev, char in nums:
                    case "", True:
                        print(f"Liczba: {res[0][0]}")
                        int_ctr += 1

                    case "", False:
                        print(f"Wyraz: {res[1][0]}")
                        chr_ctr += 1

                    case "c", True:
                        print(f"Liczba: {res[0][int_ctr]}")
                        int_ctr += 1

                    case 'i', False:
                        print(f"Wyraz: {res[1][chr_ctr]}")
                        chr_ctr += 1

                if char in nums:
                    prev = "i"
                else:
                    prev = "c"

            print()
        except EOFError:
            break
