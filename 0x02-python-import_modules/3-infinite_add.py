import sys

args = sys.argv[1:]  # exclude the first argument (the script name)
result = 0

for arg in args:
    result += int(arg)

print(result)
