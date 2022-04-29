ALPHA = "".join(map(chr, range(ord(" "), ord("я") + 1)))


def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))



if __name__ == "__main__":
    print(encode("Отче наш", 6))
    print(decode("Фшэл&ужю", 6))
