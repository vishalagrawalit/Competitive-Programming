for _ in range(int(input())):
    string = input()
    s = list(string.lower())

    add = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

    print(add)
