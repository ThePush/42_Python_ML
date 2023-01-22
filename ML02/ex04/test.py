import csvreader


def main():
    print('Test 1: good.csv')
    with csvreader.CsvReader('good.csv', header=True, skip_top=3, skip_bottom=1) as file:
        if file is not None:
            data = file.getdata()
            print(f'header: {file.getheader()}')
            for row in data:
                print(row)

    print('\nTest 2: bad.csv')
    with csvreader.CsvReader('bad.csv') as file:
        if file is not None:
            print(f'header: {file.getheader()}')
            for line in file.getdata():
                print(line)

    print('\nTest 3: file_that_doesnt_exist.csv')
    with csvreader.CsvReader('file_that_doesnt_exist.csv') as file:
        if file is not None:
            print(f'header: {file.getheader()}')
            for line in file.getdata():
                print(line)


if __name__ == "__main__":
    main()