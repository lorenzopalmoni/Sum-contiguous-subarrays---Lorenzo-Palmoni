import array as arr

# Per forza bruta: andiamo a calcolare la somma di tutti i possibili subarrays e cerchiamo il max (molto dispendioso a livello computazionale)
# differenziamo due casi particolari (banali):
#   1) quando un array ha tutti valori positivi, la soluzione è data dalla somma di tutti gli elementi dell'array
#   2) quando un array ha tutti valori negatvi, la soluzione è data dal minimo valore prensente nell'array

def sum_cont_subarr_1(array):
    """Returns the contiguous subarray which has the largest sum"""
    try:
        l = len(array)             # lunghezza array
        if l==0:                   # controllo se l'array è vuoto
            return print("The inserted array is empty, please enter a valid array.")

        sum_tot = sum(array)    # calcolo la somma di tutti gli elementi dell'array
        max_arr = max(array)    # calcolo il massimo dell'array
        i_max = 0               # inizializzo le variabili dove mettero gli indici iniziale e finale del subarray soluzione
        j_max = l



        ck_pos = all(item >= 0 for item in array)    # variabile boolean per effutare il check su positività degli elementi dell'array
        ck_neg = all(item <= 0 for item in array)    # variabile boolean per effutare il check su negatività degli elementi dell'array

        if ck_pos is True:  # check sulla positività degli elementi
            return array[i_max:j_max].tolist(), sum_tot

        if ck_neg is True:  # check sulla negatività degli elementi
            i_max = array.index(max_arr)
            return array[i_max], max_arr

        max_tot = max(sum_tot, max_arr)             # definisco max_tot, in cui andremo a storare il risultato della funzione, come il
                                                    # massimo tra le due var definite sopra in quanto nel while loop non andremo a calcolare
                                                    # i subarray di lunghezza 1 e l
        delta = 2

        while delta < l:                     # loop per incrementare la lunghezza del subarray
            i = 0
            j = delta
            while j <= l:                       # loop per incrementare gli indici posizionali dei subarray di lunghezza delta
                sum_temp = sum(array[i:j])
                if sum_temp > max_tot:
                    max_tot = sum_temp
                    i_max = i
                    j_max = j
                i += 1
                j += 1
            delta += 1
        if max_tot == max_arr:  # faccio questo controllo nel caso in cui ci sia solo un valore positivo
            i_max = array.index(max_arr)
            return array[i_max], max_arr
        else:
            return array[i_max:j_max].tolist(), max_tot
    except:
        print("Please insert a valid array.")

# The complexity of our solution is O(n^2), where n is the dimension of our sample.
# The numeber of computations grows exponentially with respect to the dimension of the sample.

########################################################################################################################

# E' possibile ottenere una soluzione con complessità lineare sfruttando l'algoritmo di Kadame
def sum_cont_subarr_2(array):
    """Returns the contiguous subarray which has the largest sum"""
    try:
        l = len(array)             # lunghezza array
        if l==0:                   # controllo se l'array è vuoto
            return print("The inserted array is empty, please enter a valid array.")

        sum_tot = sum(array)    # calcolo la somma di tutti gli elementi dell'array
        max_arr = max(array)    # calcolo il massimo dell'array
        i_max = 0               # inizializzo le variabili dove mettero gli indici iniziale e finale del subarray soluzione
        j_max = l

        ck_pos = all(item >= 0 for item in array)    # variabile boolean per effutare il check su positività degli elementi dell'array
        ck_neg = all(item <= 0 for item in array)    # variabile boolean per effutare il check su negatività degli elementi dell'array

        if ck_pos is True:  # check sulla positività degli elementi
            return array[i_max:j_max].tolist(), sum_tot

        if ck_neg is True:  # check sulla negatività degli elementi
            i_max = array.index(max_arr)
            return array[i_max], max_arr

        max_temp = max_tot = array[0]
        for i in range(1,len(array)):                    # for loop: al passo i confronta l'elemento i-esimo dell'array con la somma tra il migliore subarray di lunghezza i-1 e l'i-esimo elemento
            if array[i] > max_temp + array[i]:
                i_max = i
            max_temp = max(array[i],max_temp + array[i])
            if max_temp > max_tot:
                max_tot = max_temp
                j_max = i + 1
        if max_tot == max_arr:  # faccio questo controllo nel caso in cui ci sia solo un valore positivo
            i_max = array.index(max_arr)
            return array[i_max],max_arr
        else:
            return array[i_max:j_max].tolist(), max_tot
    except:
        print("Please insert a valid array.")
# The complexity of our solution is O(n), where n is the dimension of our sample.
# The numeber of computations grows linearly with respect to the dimension of the sample.

