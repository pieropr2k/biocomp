# --- Define tus puntuaciones ---
MATCH_SCORE = 1
MISMATCH_PENALTY = -1
GAP_PENALTY = -2

# --- Constantes para el traceback ---
DIAG = 1
UP = 2
LEFT = 3
NONE = 0 # Para Smith-Waterman

def needleman_wunsch(seq1, seq2):
    n = len(seq1)
    m = len(seq2)

    # 1. Crear matrices
    # +1 para la fila y columna de inicialización
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    trace_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # 2. Inicialización (Estilo NW)
    for i in range(1, n + 1):
        score_matrix[i][0] = i * GAP_PENALTY
        trace_matrix[i][0] = UP
    for j in range(1, m + 1):
        score_matrix[0][j] = j * GAP_PENALTY
        trace_matrix[0][j] = LEFT

    # 3. Llenar las matrices (Recurrencia)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Calcular puntuación de match/mismatch
            if seq1[i - 1] == seq2[j - 1]:
                diag_score = score_matrix[i - 1][j - 1] + MATCH_SCORE
            else:
                diag_score = score_matrix[i - 1][j - 1] + MISMATCH_PENALTY

            up_score = score_matrix[i - 1][j] + GAP_PENALTY
            left_score = score_matrix[i][j - 1] + GAP_PENALTY

            # Elegir el máximo
            scores = [diag_score, up_score, left_score]
            max_score = max(scores)

            score_matrix[i][j] = max_score

            # Guardar el camino en la matriz de traceback
            if max_score == diag_score:
                trace_matrix[i][j] = DIAG
            elif max_score == up_score:
                trace_matrix[i][j] = UP
            else: # max_score == left_score
                trace_matrix[i][j] = LEFT

    # 4. Traceback (empezar en la esquina inferior derecha)
    align1, align2 = "", ""
    i, j = n, m

    while i > 0 or j > 0:
        move = trace_matrix[i][j]

        if move == DIAG:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif move == UP:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else: # move == LEFT
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    # La puntuación final está en la última celda
    final_score = score_matrix[n][m]

    return align1, align2, final_score, score_matrix
