from ImageProcessor import ImageProcessor


def main():
    imp = ImageProcessor()
    arr = imp.load("non_existing_file.png")
    print(arr)
    arr = imp.load("empty_file.png")
    print(arr)
    arr = imp.load('../resources/42AI.png')
    print(arr)
    imp.display(arr)
    print(type(arr))


if __name__ == "__main__":
    main()