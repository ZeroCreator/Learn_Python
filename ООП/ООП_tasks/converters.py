from streams import Processor


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == "__main__":
    # obj = Uppercase(open("spam.txt"), sys.stdout)
    # obj.process()
    import converters
    prog = converters.Uppercase(open("spam.txt"), open("spamup.txt", "w"))
    prog.process()
