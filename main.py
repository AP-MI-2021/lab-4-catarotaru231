def show_menu():

    '''
    Prezinta interfata principala
    :return:
    '''
    print('''
1. Citirea unei liste de numere întregi. Citirile repetate suprascriu listele precedente.

2. Afișarea tuturor numerelor negative nenule din listă (de ex. -1, -56).

3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.

4. Afișarea tuturor numerelor din listă care sunt superprime. Un număr este superprim dacă este
strict pozitiv și toate prefixele sale sunt prime. De exemplu, 173 nu este superprim deoarece 1 nu
este prim, iar 239 este superprim deoarece 2, 23 și 239 sunt toate prime.

5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
x. Iesire din meniu
''')

def citire_lista():

    '''
    se citeste numarul de elemente intregi si elementele din lista
    :return:
    '''

    lst = []
    n = int(input("Numarul de elemente citite este: "))
    print("Elementele citite sunt:")
    for i in range(n):
        ele = int(input())
        lst.append(ele)
    return lst

def afisare_numere_negative(lst):

    '''
    se identifica si se retin elementele negative din lista intr-o alta lista, pe care o afisam
    :param lst:
    :return:
    '''

    rez = []
    for i in lst:
        if(i < 0):
            rez.append(i)
    return rez

def test_afisare_numere_negative():
    assert afisare_numere_negative([-1]) == [-1]
    assert afisare_numere_negative([]) == []
    assert afisare_numere_negative([1, 2, 3, 4, -5, -16, 0]) == [-5, -16]

def cel_mai_mic_numar(lst):

    '''
    Se determina cel mai mic numar care are ultima cifra o cifra citita la tastatura si se retine
    :param lst:
    :return:
    '''

    c = int(input("Cifra citita de la tastatura este: "))
    nr = 0
    for i in lst:
        if(i % 10 == c):
            nr = i
    for i in lst:
        if(i % 10 == c):
            if(i < nr):
                nr = i
    return nr

def test_cel_mai_mic_numar():

    '''
    nu se pot face teste concrete deoarece nu avem o valoare exacta pe care putem lucra
    :return:
    '''

    pass

def nr_prim(n):

    '''
    determinam daca un numar este prim
    :param n:
    :return:
    '''

    if(n < 2):
        return False
    for i in range(2, n//2 + 1):
        if(n % i == 0):
            return False
    return True

def nr_superprim(n):

    '''
    determinam daca un numar este superprim
    :param n:
    :return:
    '''

    while n > 0:
        if(nr_prim(n) == False):
            return False
        n //=10
    return True

def test_nr_superprim():
    assert nr_superprim(173) == False
    assert nr_superprim(239) == True
    assert nr_superprim(1000) == False

def afisare_numere_superprime(lst):

    '''
    se identifica numere superprime din lista si se retin intr-o lista separata.
    :param lst:
    :return:
    '''

    rez = []
    for i in lst:
        if(nr_superprim(i) == True):
            rez.append(i)
    return rez

def test_afisare_numere_superprime():
    assert afisare_numere_superprime([173,239,9]) == [239]
    assert afisare_numere_superprime([]) == []
    assert afisare_numere_superprime([239,11,293]) == [239,293]

def nr_negative(n):

    '''
    Numarul negativ prelucrat va fi schimbat cu versiunea sa cu cifre inversa
    Daca numarul este pozitiv, se va returna -1
    :param n:
    :return:
    '''

    if(n >= 0):
        return -1
    n = n*-1
    cn = 0
    while(n):
        cn = cn * 10 + n % 10
        n //= 10
    cn = cn * -1
    return cn

def test_numere_negative():
    assert nr_negative(-16) == -61
    assert nr_negative(100) == -1
    assert nr_negative(-1934) == -4391
    assert nr_negative(0) == -1

def cmmdc(a,b):

    '''
    Algoritm specific CMMDC
    '''

    if(b==0):
        return a
    else:
        return cmmdc(b,a%b)

def cmmdc_lista(lst):

    '''
    Se realizeaza CMMDC al tuturor elementelor dintr-o lista
    :param lst:
    :return:
    '''

    n = cmmdc(lst[0],lst[1])
    for i in range(2,len(lst)):
        n = cmmdc(n,lst[i])
    return n

def lista_prelucrata(lst):

    '''
    numerele pozitive si nenule din lista sunt inlocuite cu CMMDC-ul lor si cele negative cu cifrele in ordine inversa
    :param lst:
    :return:
    '''

    temp = []
    for i in range(len(lst)):
        if(lst[i] > 0):
            temp.append(lst[i])
        else:
            lst[i] = nr_negative(lst[i])
    for i in range(len(lst)):
        if(lst[i] > 0):
            lst[i] = cmmdc_lista(temp)
    return lst

def test_lista_prelucrata():
    assert lista_prelucrata([-76, 12, 24, -13 ,144 ]) == [-67, 12, 12, -31, 12]
    assert lista_prelucrata([-29, 100, 50, 25, -144]) == [-92, 25, 25, 25, -441]
    assert lista_prelucrata([]) == []

def main():
    lst = []
    while True:
        show_menu()
        P = input("Selectati problema pe care doriti sa o rezolvati: ")
        if(P == '1'):
            lst = citire_lista()
        elif(P == '2'):
            print("Numerele negative din lista sunt:",
                afisare_numere_negative(lst))
        elif(P == '3'):
            print("Cel mai mic numar din lista care are ultima cifra o cifra citita de la tastatura este:",
                cel_mai_mic_numar(lst))
        elif(P == '4'):
            print("Numerele din lista care sunt superprime sunt:",
                  afisare_numere_superprime(lst))
        elif(P == '5'):
            print("Lista noua obtinuta din lista initiala este:",
                  lista_prelucrata(lst))
        elif(P == 'x'):
            break
        else:
            print("Comanda gresita. Reincercati")
test_afisare_numere_superprime()
test_cel_mai_mic_numar()
test_nr_superprim()
test_numere_negative()
test_afisare_numere_negative()
test_lista_prelucrata()
main()

