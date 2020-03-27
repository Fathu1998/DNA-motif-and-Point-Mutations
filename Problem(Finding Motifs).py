A=input("Enter the DNA sequence")
print("Thus the DNA sequence is", A)
B=input("Now enter the DNA motif that you wish to find")
print("Thus the motif that you wish to find is",B)
Mot=0
for i in range (len(A)-len(B)+1):
    if B==A[i:len(B)]:
        Mot+=1
print("Thus the positions of the motif are", Mot)


        
    
