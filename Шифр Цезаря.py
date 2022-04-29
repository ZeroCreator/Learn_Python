ALPHA = "".join(map(chr, range(ord(" "), ord("я") + 1)))


def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))



if __name__ == "__main__":
    r = encode("Отче наш", 6)
    print(r)
    print(decode(r, 6))
