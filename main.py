
def main():
    print(' '.join(arrizer(prompt)))


def arrizer(input):
    arr = input.split(' ')
    arr2 = []

    for i in arr:
        if i not in arr2:
            arr2.append(i)
        else:
            continue
    return arr2


if __name__ == '__main__':
    prompt = input("Input a word ")
    main()
