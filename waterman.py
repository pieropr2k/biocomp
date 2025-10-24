# --- Define tus puntuaciones ---
MATCH_SCORE = 1
MISMATCH_PENALTY = -1
GAP_PENALTY = -2

# --- Constantes para el traceback ---
DIAG = 1
UP = 2
LEFT = 3
NONE = 0 # Para Smith-Waterman

def smith_waterman(seq1, seq2):
    # ... (La estructura es muy similar)
    # 1. Crear matrices

    # 2. Inicialización (Estilo SW)
    # ¡No haces nada! Ya están en 0.

    # Variables para guardar el máximo
    max_score = 0
    max_i, max_j = 0, 0

    # 3. Llenar las matrices (Recurrencia SW)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # ... (calcular diag_score, up_score, left_score igual que en NW)

            # ¡La gran diferencia!
            scores = [diag_score, up_score, left_score, 0] # Añadir 0
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

    # 4. Traceback (empezar en (max_i, max_j))
    align1, align2 = "", ""
    i, j = max_i, max_j

    # Terminar cuando llegues a un 0
    while trace_matrix[i][j] != NONE:
        move = trace_matrix[i][j]
        # ... (construir alineamiento igual que en NW)
        # ... (mover i, j)

    return align1, align2, max_score