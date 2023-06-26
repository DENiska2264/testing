def palind():
    n = str(input("вуведите слово: "))
    s = str(n)
    l = len(s)
    for i in range(l//2):
        if s[i] != s[-1-i]:
            print("не палиндром")
            break
        else:
            print("палиндром")



palind()