A=input("Enter A DNA sequence")
print(A)
B=input("Enter another DNA sequence")
print(B)
Hamming_Count=0
if len(A)==len(B):
    for i in range (len(A)):
        if A[i]!= B[i]:
            Hamming_Count +=1
print("The Hamming count of the given 2 DNA sequences is",Hamming_Count)
