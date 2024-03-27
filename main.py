import pickle

letter_cods = {0:'н', 1:'г', 2:'к', 3:'т', 4:'ч', 5:'п', 6:'ш', 7:'с', 8:'в', 9:'д'}
number_cods = {i:[letter_cods[int(str(i)[0])], letter_cods[int(str(i)[1])]] for i in range(10, 101)}

with open('words.txt','rb') as inp:
    words = pickle.load(inp)

for number, code in number_cods.items():
    s = ['б','в','г','д','ж','з','к','л','м','н','п','р','с','т','ф','х','ч','ц','ш','щ']
    s.remove(code[0])
    if code[0] != code[1]:
        s.remove(code[1])

    print(number)

    for i in words[code[0].upper()]:

        if code[0] != code[1]:
            if not(set(map(str, i)) & set(s)) and code[1] in i and i.count(code[1]) == i.count(code[0]) == 1:
                print(i)

        else:
            if not(set(map(str, i)) & set(s)) and code[1] in i and i.count(code[1]) == 2:
                print(i)

    print('\n')
