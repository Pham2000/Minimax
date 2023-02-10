from ast import ImportFrom


class Board:
    def __init__(self, N, M, H):
        #N is number of cols/rows in n x n grid
        #M is number of disks to connect contiguously 
        #H is who makes the first move (1 = computer, 0 = human)
        print(N, M, H)

        self.N = N
        while self.N < 3 or self.N > 10:
            print('Error: invalid board size')
            print('Parameters (3 <= N <= 10)')
            self.N = int(input('Please enter a new board size: '))

        self.M = M
        while self.M <= 1 or self.M > N:
            print('Error: invalid disks value')
            print('Parameters (1 < M <= N)')
            self.M = int(input('Please enter a new disk value: '))
        
        self.H = H
        while self.H != 0 and self.H != 1:
            print('Error: invalid starting player')
            print('Parameters (H == 1 or H == 0)')
            self.H = int(input('Please enter a new starting player: '))

        board = [N][N]

    #idk if this how you want it
    def gameplay():
        
        if(H == 0):
            humanKey = 'o'
            aiKey = 'x'
            while 1:
                if H == 0:
                    #human make move
                    H = 1
                elif H == 1:
                    #ai make move
                    H = 0

        elif(H == 1):
            humankey = 'x'
            aiKey = 'o'
            while 1:
                if H == 1:
                    #ai make move
                    H = 0
                elif H == 0:
                    #human make move
                    H = 1

    #print board
    def printBoard(N):
        print("+" + "---+" * N)
        for i in range(N):
            print("|", end="")
            for g in range(N):
                print(" {} |".format(g),end="")
            print("\n+" + "---+" * N)



    
   