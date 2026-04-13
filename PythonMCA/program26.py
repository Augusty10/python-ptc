for i in range(1, 10):
    if i == 3:
        print("Skipped 3")
        continue
    if i == 6:
        print("Loop stopped at 6")
        break
    print(i)
    