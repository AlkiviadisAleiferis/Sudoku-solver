from sys import path
path.append("e:\\python\\lib\\site-packages")
path.append("C:\\Users\\alkiv\\AppData\Roaming\\Python\\Python39\\site-packages")

from ortools.sat.python import cp_model
model=cp_model.CpModel()

def sudoku_solver(sudoku_start):
        Xij=[]
        row_i=[]
        col_j=[]

        for i in range(9):
            Xij.append([])
            for j in range(9):
                Xij[i].append(model.NewIntVar(1,9,'X'+str(i)+str(j)))


        for i in range(9):
            row_i = Xij[i]

            model.AddAllDifferent(row_i)


        for j in range(9):
            col_j = []
            for i in range(9):
                col_j.append(Xij[i][j])

            model.AddAllDifferent(col_j)

        square=[]
        for sq in range(9):
            square.append([])
            for i in range(3):
                for j in range(3):
                    if sq==0 or sq==3 or sq==6:
                        square[sq].append(Xij[i+sq][j])
                    if sq == 1 or sq == 4 or sq == 7:
                        square[sq].append(Xij[i + sq -1][j+3])
                    if sq == 2 or sq == 5 or sq == 8:
                        square[sq].append(Xij[i + sq -2][j+6])

            model.AddAllDifferent(square[sq])

        # sudoku= [ [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0],
        #           [ 0 , 0 , 0,    0, 0, 0,    0, 0, 0]]
        sudoku=sudoku_start[:]
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] != 0 :
                    model.Add(Xij[i][j]==sudoku[i][j])


        solver = cp_model.CpSolver()

        status=solver.Solve(model)
        solution_print=''
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
                for i in range(9):
                    solution_print+='\n'
                    for j in range(9):
                        solution_print+=str(solver.Value(Xij[i][j]))+'  '
                        if j==2 or j==5:
                            solution_print+='   '
                        if j==8 and (i==2 or i==5):
                            solution_print+='\n\n'
        else:
            solution_print+='no solution, check input numbers'

        return solution_print

