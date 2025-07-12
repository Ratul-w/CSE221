T=int(input())
for i in range(T):
  H=input()
  B=H.split()
  if B[2]=='+':
    print(int(B[1])+ int(B[3]))
  elif B[2]=='-':
    print(int(B[1])- int(B[3]))
  elif B[2]=='/':
    print(int(B[1])/ int(B[3]))
  elif B[2]=='*':
    print(int(B[1])* int(B[3]))