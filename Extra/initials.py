def main():
    name = input("Whats Your First Name?:")
    name2 = input("And your last name?:")
    name = ""
    name2 = ""

    if name and name2 != int:
        print(name[0], name2[0])
    else:
        print("Please write your name in letters")


if __name__ == "__main__":
    main()

