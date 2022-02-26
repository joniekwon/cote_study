import sys
N = int(sys.stdin.readline())
num_dict = {}
for i in range(N):
   key = int(sys.stdin.readline())
   try:
      num_dict[key] += 1
   except:
      num_dict[key] = 1
for k, v in sorted(num_dict.items(), key=lambda x:x[0]):
   for i in range(num_dict[k]):
      print(k)