import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.game_over = False
        self.draw_board()
        
    def draw_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Helvetica", 20), width=3, height=1, command=lambda row=i, col=j: self.play_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    
    def play_move(self, row, col):
        if self.game_over or self.board[row][col] != ' ':
            return
        
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        
        if self.check_win(row, col):
            self.game_over = True
            self.show_message(f"Le joueur {self.current_player} a gagné!")
        elif self.check_draw():
            self.game_over = True
            self.show_message("Match nul!")
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_win(self, row, col):
        return self.check_row(row) or self.check_column(col) or self.check_diagonal() or self.check_antidiagonal()
    
    def check_row(self, row):
        return self.board[row][0] == self.board[row][1] == self.board[row][2] != ' '
    
    def check_column(self, col):
        return self.board[0][col] == self.board[1][col] == self.board[2][col] != ' '
    
    def check_diagonal(self):
        return self.board[0][0] == self.board[1][1] == self.board[2][2] != ' '
    
    def check_antidiagonal(self):
        return self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '
    
    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False
        return True
    
    def show_message(self, message):
        popup = tk.Toplevel()
        label = tk.Label(popup, text=message, font=("Helvetica", 20))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(popup, text="Rejouer", command=self.reset)
        button.pack()
    
    def reset(self):
        self.current_player = 'X'
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.game_over = False
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        
        self.master.destroy()
        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()



def ia(board, signe):
    """
    Retourne l'emplacement où l'IA souhaite jouer (0-8) en utilisant l'algorithme de minimax.
    """
    joueur = 1 if signe == "X" else 2
    adversaire = 2 if signe == "X" else 1

    def evaluer_etat(etat):
        """
        Évalue l'état du plateau de jeu et retourne un score correspondant à la qualité du
        plateau pour le joueur actuel.
        """
        if etat["gagnant"] == joueur:
            return 1
        elif etat["gagnant"] == adversaire:
            return -1
        else:
            return 0

    def minimax(etat, joueur_actuel):
        """
        Implémente l'algorithme minimax pour trouver le meilleur coup à jouer.
        """
        if etat["gagnant"] is not None:
            return evaluer_etat(etat)

        if joueur_actuel == joueur:
            meilleur_score = float("-inf")
            for coup in etat["coups_possibles"]:
                etat_suivant = etat.copy()
                etat_suivant["plateau"][coup] = joueur
                etat_suivant["coups_possibles"].remove(coup)
                score = minimax(etat_suivant, adversaire)
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup
            return meilleur_score if meilleur_score != float("-inf") else 0
        else:
            meilleur_score = float("inf")
            for coup in etat["coups_possibles"]:
                etat_suivant = etat.copy()
                etat_suivant["plateau"][coup] = adversaire
                etat_suivant["coups_possibles"].remove(coup)
                score = minimax(etat_suivant, joueur)
                if score < meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup
            return meilleur_score if meilleur_score != float("inf") else 0

    etat_initial = {"plateau": board.copy(), "coups_possibles": [i for i, x in enumerate(board) if x == 0], "gagnant": None}
    score_max = float("-inf")
    meilleur_coup = None
    for coup in etat_initial["coups_possibles"]:
        etat_suivant = etat_initial.copy()
        etat_suivant["plateau"][coup] = joueur
        etat_suivant["coups_possibles"].remove(coup)
        score = minimax(etat_suivant, adversaire)
        if score > score_max:
            score_max = score
            meilleur_coup = coup

    return meilleur_coup if meilleur_coup is not None else False
