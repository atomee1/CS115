

class Board(object):

    def createRow(self,width):
        '''Returns one row of blanks of width'''
        row = []
        for col in range(width):
            row += ' '
        return row

    def createBoard(self,width,height):
        '''Returns 2D array with 'height' rows and 'width' cols'''
        newBoard = []
        for row in range(height):
            newBoard += [self.createRow(width)]
        return newBoard

    def __init__(self, width = 7, height = 6):
        '''Initializes new Board object'''
        self.cols = width
        self.rows = height
        self.board = self.createBoard(width,height)

    def __str__(self):
        newBoard = ""
        for row in range(self.rows):
            for col in range(self.cols):
                newBoard += '|' + self.board[row][col]
                if col == self.cols - 1:
                    newBoard+= '|\n'
        newBoard += ('-' * (self.cols*2)) + '\n' + ' '
        for i in range(self.cols):
            newBoard += str(i) + ' '
        return newBoard

    def allowsMove(self,col):
        '''Returns True if Board object allows a move into column c'''
        return (col >= 0 and col < self.cols) and self.board[0][col] == ' '

    def addMove(self,col,ox):
        '''Assuming Board object allows move, add ox marker to highest empty row in col'''
        curRow = self.rows - 1
        while not self.board[curRow][col] == ' ':
            curRow -= 1
        self.board[curRow][col] = ox

    def setBoard(self,moveString):
        '''Takes in a string of columns and places alternating checkers in those columns, starting with 'X' '''
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.cols:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
    
    def delMove(self, col):
        '''Removes the top checker from col'''
        if self.board[self.rows - 1][col] != ' ':
            curRow = 0
            while self.board[curRow][col] == ' ':
                curRow += 1
            self.board[curRow][col] = ' '

    def horizontal(self,ox,row,col):
        '''Returns True if mark ox has 4 consecutive matches horizontally'''
        count = 0
        while count < 4 and col < self.cols and self.board[row][col] == ox:
            count += 1
            col += 1
        return count == 4

    def vertical(self,ox,row,col):
        '''Returns True if mark ox has 4 consecutive matches vertically'''
        count = 0
        while count < 4 and row < self.rows and self.board[row][col] == ox:
            count += 1
            row += 1
        return count == 4

    def diagonalE(self,ox,row,col):
        '''Returns True if mark ox has 4 consecutive matches diagonally (right downwards)'''
        count = 0
        while count < 4 and row < self.rows and col < self.cols and self.board[row][col] == ox:
            count += 1
            row += 1
            col += 1
        return count == 4

    def diagonalW(self,ox,row,col):
        '''Returns True if mark ox has 4 consecutive matches diagonally (right downwards)'''
        count = 0
        while count < 4 and row < self.rows and col >= 0 and self.board[row][col] == ox:
            count += 1
            row += 1
            col -= 1
        return count == 4

    def winsFor(self,ox):
        '''Returns True if mark ox scores 4 matches in a row in any direction'''
        for row in range(self.rows):
            for col in range(self.cols):
                if self.horizontal(ox,row,col) or self.vertical(ox,row,col) or self.diagonalE(ox,row,col) or self.diagonalW(ox,row,col):
                    return True
        return False

    def full(self):
        '''Returns True if Board object is full'''
        for col in range(self.cols):
            if self.board[0][col] == ' ':
                return False
        return True

    def hostGame(self):
        '''Runs loop hosting a game of Connect Four on the Board object'''
        print('Welcome to Connect Four!')

        x = 'X'
        o = 'O'
        player = x

        while not self.winsFor(x) and not self.winsFor(o) and not self.full():
            print(self)
            choice = int(input(player + "'s choice: "))
            
            if self.allowsMove(choice):
                self.addMove(choice,player)
                
                if self.winsFor(player):
                    print(player + " wins! Congratulations!")
                    print(self)
                elif player == x:
                    player = o
                else:
                    player = x
