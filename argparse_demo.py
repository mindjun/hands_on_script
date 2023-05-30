import argparse

print('this is a demo')
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity", choices=[1, 2, 3], default=1)
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on :{}".format(args.verbosity ** 2))
