#Made by Prithwish Mukherjee
print("------------------------------------------------------")
print("Decimal to Binary calculater by")
print("Prithwish Mukherjee ")
print("------------------------------------------------------")


def decimalToBinary(n):
    return bin(n).replace("Ob", "")


if __name__ == "__main__":
    inp = int(input("Enter any number to be converted \n"))
    print(decimalToBinary(inp))
