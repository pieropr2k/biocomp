def smith_waterman(seq1, seq2, match=1, mismatch=0, gap=-1):
    """
    Realiza un alineamiento local de secuencias usando el algoritmo de Smith-Waterman.

    Argumentos:
    seq1 (str): La primera secuencia (se colocará en las filas, vertical).
    seq2 (str): La segunda secuencia (se colocará en las columnas, horizontal).
    match (int): Puntuación por una coincidencia (match).
    mismatch (int): Puntuación por una no coincidencia (mismatch).
    gap (int): Penalización por un espacio (gap).

    Devuelve:
    (str, str, int): Una tupla con (alineamiento1, alineamiento2, puntaje_maximo)
    """

    ### 1. Definir constantes para el traceback ###
    NONE = 0  # Parar el traceback
    DIAG = 1  # Moverse en diagonal
    UP = 2    # Moverse hacia arriba
    LEFT = 3  # Moverse hacia la izquierda

    n = len(seq1)
    m = len(seq2)

    ### 2. Crear e inicializar matrices ###
    # La matriz de puntajes (score_matrix) se inicializa toda en 0
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    # La matriz de trazado (trace_matrix) también
    trace_matrix = [[NONE] * (m + 1) for _ in range(n + 1)]

    # Variables para guardar el máximo puntaje y su posición
    max_score = 0
    max_i, max_j = 0, 0

    ### 3. Llenar las matrices ###
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            ### CÁLCULO DE PUNTAJES (COMPLETADO) ###
            
            # Puntaje por match/mismatch (diagonal)
            match_mismatch_score = match if seq1[i-1] == seq2[j-1] else mismatch
            diag_score = score_matrix[i-1][j-1] + match_mismatch_score
            
            # Puntaje por gap en seq1 (arriba)
            up_score = score_matrix[i-1][j] + gap
            
            # Puntaje por gap en seq2 (izquierda)
            left_score = score_matrix[i][j-1] + gap

            ### ¡La gran diferencia de SW! ###
            # Comparamos también con 0
            scores = [diag_score, up_score, left_score, 0] 
            max_score_cell = max(scores)

            score_matrix[i][j] = max_score_cell

            # Guardar el camino
            if max_score_cell == diag_score:
                trace_matrix[i][j] = DIAG
            elif max_score_cell == up_score:
                trace_matrix[i][j] = UP
            elif max_score_cell == left_score:
                trace_matrix[i][j] = LEFT
            else: # max_score_cell == 0
                trace_matrix[i][j] = NONE

            # Actualizar el máximo global
            if max_score_cell > max_score:
                max_score = max_score_cell
                max_i, max_j = i, j

    ### 4. Traceback ###
    align1, align2 = "", ""
    i, j = max_i, max_j

    # Terminar cuando llegues a un 0 (NONE)
    while trace_matrix[i][j] != NONE:
        move = trace_matrix[i][j]
        
        ### LÓGICA DE TRACEBACK (COMPLETADO) ###
        if move == DIAG:
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif move == UP:
            align1 += seq1[i-1]
            align2 += "-"
            i -= 1
        elif move == LEFT:
            align1 += "-"
            align2 += seq2[j-1]
            j -= 1
    
    print(trace_matrix)
    print(score_matrix)
    print(align1)
    # Como construimos los alineamientos al revés, les damos la vuelta
    return align1[::-1], align2[::-1], max_score

# --- EJEMPLO DE USO ---
# Usando los datos de la imagen que me mostraste
seq_i = "GGTTGACTA"       # Tu "Secuencia i"
seq_j = "TGTTACGG"   # Tu "Secuencia j"

#seq_i = "ACGAT"       # Tu "Secuencia i"
#seq_j = "ATTCGATCC"   # Tu "Secuencia j"


# Parámetros de la imagen
match = 1
mismatch = 0
gap = -1

# Ejecutar el algoritmo
alineamiento1, alineamiento2, puntaje = smith_waterman(seq_i, seq_j, match, mismatch, gap)

print(f"Secuencia i: {seq_i}")
print(f"Secuencia j: {seq_j}")
print("---")
print(f"Mejor alineamiento local encontrado:")
print(f"Alineamiento i: {alineamiento1}")
print(f"Alineamiento j: {alineamiento2}")
print(f"Puntaje: {puntaje}")