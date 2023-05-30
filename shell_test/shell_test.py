def main(a, b):
    if int(a) > int(b):
        print('ok')
        sys.exit(0)
    else:
        try:
            1/0
        except Exception as ex:
            print(ex)
            print('failed')
            sys.exit(1)


if __name__ == '__main__':
    import sys
    args = sys.argv
    main(*args[1:])

