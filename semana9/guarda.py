# def geraPrimos(n,C,P,np):


# def ehPrimo(n, P, np):
#     for i in range(np): #1 a np+1
#         if(n%p[i] == 0):
#             if(n != P[i]):
#                 return False
#             else:
#                 return True
#     return True

# def ehComposto(primo):
#     if(primo):
#         return 'N'
#     else:
#         return 'S'

# #-------------------------------------

# def fatora(n,P,np,F,nf):
#     nf = 0
#     for i in range(np): #1 a np+1
#         while(n%p[i] == 0):
#             nf += 1
#             F[nf] = P[i]
#             n = n/P[i]
#         if(n == 1 or P[i] >= [math.sqrt(n)]):
#             break
#     if(n != 1):
#         nf += 1
#         F[nf] = n
#     return F

# def divisores(n,F,nf,D,nd):
#     F[0],nd,D[1] = 1,1,1
#     for i in range(1,nf+1):
#         if(F[i] == F[i-1]):
#             k *= F[i]
#         else:
#             k = F[i]
#             nda = nd
#         for j in range(1,nda+1): 
#             nd += 1
#             D[nd] = k*D[j]
#     return D
