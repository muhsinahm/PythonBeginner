#a program to detect double space in a string
import re
txt = input("write strings with double spaces ")
x = txt.count("  ")

print(f"number of double spacs {x}")

replaced_txt = re.sub(r"\s{2,}", " ", txt)

print("Cleaned text:")
print(replaced_txt)