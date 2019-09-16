import exact_cover
import sudoku
import killer
import algorithm_dlx

import time
import numpy as np 

class Timer():
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('\n' + self.name)
        self.start_time = time.process_time()

    def __exit__(self, type, value, traceback):
        elapsed = time.process_time() - self.start_time
        print('\n' + self.name + ' took ' + str(elapsed) + ' seconds\n')

test_matrix_1 = np.array([
    [0,0,0,0,1,0,0],
    [1,0,0,1,0,0,1],
    [0,1,1,0,0,1,0],
    [1,0,0,1,0,1,0],
    [0,1,1,0,1,1,0]])

test_matrix_2 = np.array([
    [1,0,0,0,1],
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0]])

test_matrix_3 = np.array([
    [1,0,0,1,0,0],
    [1,0,0,0,1,0],
    [0,1,1,0,0,1],
    [0,0,0,1,0,1],
    [0,1,1,0,0,0]])

test_matrix_4 = np.array([
    [0,1,0,0,1,0,1],
    [0,0,0,1,0,0,1],
    [1,1,0,0,0,1,0],
    [1,0,0,1,0,0,0],
    [0,0,1,0,0,1,0],
    [0,1,1,1,1,1,0]])

test_matrix_5 = np.array([
    [0,1,0,0,1,0,1,0,0,1],
    [0,0,0,1,0,0,1,0,0,1],
    [1,0,1,0,0,1,0,1,0,0],
    [1,0,0,1,0,0,0,0,1,0],
    [0,0,1,0,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,0,0,0]])

test_sudoku_1 = np.array([
    [0,0,3,0,1,0,0,0,0],
    [4,1,5,0,0,0,0,9,0],
    [2,0,6,5,0,0,3,0,0],
    [5,0,0,0,8,0,0,0,9],
    [0,7,0,9,0,0,0,3,2],
    [0,3,8,0,0,4,0,6,0],
    [0,0,0,2,6,0,4,0,3],
    [0,0,0,3,0,0,0,0,8],
    [3,2,0,0,0,7,9,5,0]])

test_sudoku_2 = np.array([
    [0,0,0,0,0,0,6,8,0],
    [0,0,0,0,7,3,0,0,9],
    [3,0,9,0,0,0,0,4,5],
    [4,9,0,0,0,0,0,0,0],
    [8,0,3,0,5,0,9,0,2],
    [0,0,0,0,0,0,0,3,6],
    [9,6,0,0,0,0,3,0,8],
    [7,0,0,6,8,0,0,0,0],
    [0,2,8,0,0,0,0,0,0]])

test_sudoku_3 = np.array([
    [0,2,6,0,0,0,8,1,0],
    [3,0,0,7,0,8,0,0,6],
    [4,0,0,0,5,0,0,0,7],
    [0,5,0,1,0,7,0,9,0],
    [0,0,3,9,0,5,1,0,0],
    [0,4,0,3,0,2,0,5,0],
    [1,0,0,0,3,0,0,0,2],
    [5,0,0,2,0,4,0,0,9],
    [0,3,8,0,0,0,4,6,0]])

test_sudoku_4 = np.array([
    [0,0,2,0,5,7,0,4,0],
    [0,4,0,3,0,6,8,0,1],
    [0,0,0,2,0,4,3,7,5],
    [0,1,0,0,0,0,7,8,0],
    [0,0,0,8,0,0,0,0,0],
    [9,0,4,0,7,0,0,5,0],
    [0,0,0,0,1,5,0,0,6],
    [0,0,9,7,6,0,0,0,0],
    [5,0,0,0,0,8,0,0,0]])

test_sudoku_5 = np.array([
    [8,7,0,0,4,0,3,0,0],
    [0,1,2,7,3,0,8,0,0],
    [0,3,9,0,0,1,0,6,7],
    [0,9,0,0,5,0,7,0,0],
    [0,0,0,6,0,9,0,0,0],
    [0,0,5,0,1,0,0,9,0],
    [9,5,0,3,0,0,4,2,0],
    [0,0,1,0,2,4,9,7,0],
    [0,0,4,0,9,0,0,8,5]])

test_sudoku_6 = np.array([
    [0,0,5,0,7,0,8,1,0],
    [0,0,3,0,0,1,0,0,0],
    [0,1,0,8,0,0,0,6,2],
    [0,2,0,0,1,0,7,0,0],
    [6,0,0,0,5,0,0,0,3],
    [0,0,1,0,9,0,0,2,0],
    [9,3,0,0,0,7,0,8,0],
    [0,0,0,9,0,0,2,0,0],
    [0,5,2,0,3,0,9,0,0]])

test_sudoku_7 = np.array([
    [0,0,0,0,0,4,7,0,3],
    [7,4,0,3,0,0,0,1,0],
    [8,0,0,1,5,7,0,9,6],
    [0,8,4,0,7,2,5,0,0],
    [0,0,0,0,3,0,0,0,0],
    [6,0,3,5,4,9,0,0,0],
    [0,0,8,0,0,0,0,0,0],
    [0,0,0,7,0,0,0,8,0],
    [0,6,0,0,2,0,0,0,4]])

test_sudoku_8 = np.array([
    [0,6,0,7,0,0,0,0,0],
    [3,0,2,5,0,0,8,0,0],
    [1,0,0,0,0,0,0,2,4],
    [0,0,0,0,2,0,9,0,0],
    [8,0,1,0,0,4,2,7,0],
    [0,0,0,1,0,7,0,0,0],
    [0,0,0,0,0,0,3,0,0],
    [7,0,0,8,5,0,6,0,0],
    [0,0,0,0,0,0,0,4,9]])

test_sudoku_9 = np.array([
    [0,0,0,0,0,4,0,0,0],
    [0,0,6,0,0,0,0,0,0],
    [0,0,0,3,9,0,7,0,5],
    [0,7,4,0,0,0,0,6,0],
    [0,8,0,0,0,3,0,0,9],
    [9,0,2,0,1,0,3,7,0],
    [0,3,1,6,0,0,9,0,0],
    [0,0,9,0,0,0,0,0,0],
    [0,0,0,5,4,0,6,0,0]])

test_sudoku_10 = np.array([
    [0,8,0,0,0,0,0,3,0],
    [7,0,4,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,6,0],
    [0,0,1,0,0,6,0,0,0],
    [9,0,0,3,4,0,0,0,0],
    [0,7,0,8,0,0,2,0,0],
    [0,0,8,0,0,3,4,2,0],
    [0,4,0,0,0,0,9,1,0],
    [0,0,0,2,5,0,0,0,0]])

test_killer_1_matrix = np.array([
    ['A','A','B','B','B','C','D','E','F'],
    ['G','G','H','H','C','C','D','E','F'],
    ['G','G','I','I','C','J','K','K','F'],
    ['L','M','M','I','N','J','K','O','F'],
    ['L','P','P','Q','N','J','O','O','R'],
    ['S','P','T','Q','N','U','V','V','R'],
    ['S','T','T','Q','W','U','U','X','X'],
    ['S','Y','Z','W','W','a','a','X','X'],
    ['S','Y','Z','W','b','b','b','c','c']])
test_killer_1_sums = {
    'A': 3, 
    'B': 15, 
    'C': 22, 
    'D': 4,
    'E': 16, 
    'F': 15, 
    'G': 25,
    'H': 17,
    'I': 9,
    'J': 8, 
    'K': 20,
    'L': 6, 
    'M': 14, 
    'N': 17, 
    'O': 17, 
    'P': 13,
    'Q': 20,
    'R': 12,
    'S': 27,
    'T': 6,
    'U': 20,
    'V': 6,
    'W': 10,
    'X': 14,
    'Y': 8,
    'Z': 16,
    'a': 15,
    'b': 13,
    'c': 17}

#1 second set up 0.2 second solve
test_killer_2_matrix = np.array([
    ['A','A','B','B','B','C','D','E','F'],
    ['A','J','K','K','K','C','D','E','F'],
    ['M','J','L','L','V','C','D','H','H'],
    ['M','R','U','L','V','V','G','G','I'],
    ['N','R','U','g','g','g','f','Z','I'],
    ['N','S','S','d','d','e','f','Z','W'],
    ['O','O','T','b','d','e','e','Y','W'],
    ['P','Q','T','b','c','c','c','Y','X'],
    ['P','Q','T','b','a','a','a','X','X']])
test_killer_2_sums = {   
                        'A': 13, 'B': 14, 'C': 24, 'D': 17, 
                        'E': 13, 'F': 10, 'G': 15, 'H': 5, 'I': 11, 
                        'J': 12, 'K': 7, 'L': 17, 'M': 6, 'N': 8, 
                        'O': 9, 'P': 17, 'Q': 4, 'R': 17, 'S': 11, 
                        'T': 15, 'U': 4, 'V': 11, 'W': 14, 'X': 11, 
                        'Y': 16, 'Z': 4, 'a': 18, 'b': 19, 'c': 12, 
                        'd': 16, 'e': 8, 'f': 7, 'g': 20
                    }

#10 second setup
test_killer_3_matrix = np.array([
                            ['A','A','A','D','E','E','E','F','F'],
                            ['B','B','D','D','E','H','F','F','G'],
                            ['B','C','C','K','L','H','H','G','G'],
                            ['I','I','K','K','L','O','N','N','M'],
                            ['I','J','J','O','O','O','N','N','M'],
                            ['I','J','J','O','U','V','V','M','M'],
                            ['P','P','R','R','U','V','W','W','Y'],
                            ['P','Q','Q','R','S','T','T','Y','Y'],
                            ['Q','Q','S','S','S','T','X','X','X']])
test_killer_3_sums = {
    'A': 9, 'B': 17, 'C': 11, 'D': 12, 
                'E': 25, 'F': 23, 'G': 8, 'H': 19, 'I': 18, 
                'J': 20, 'K': 22, 'L': 5, 'M': 11, 'N': 30, 
                'O': 26, 'P': 20, 'Q': 21, 'R': 13, 'S': 11, 
                'T': 18, 'U': 15, 'V': 9, 'W': 7, 'X': 12, 
                'Y': 23}

test_killer_4_matrix = np.array([
    ['A','B','B','C','D','D','E','F','G'],
    ['A','B','B','C','D','H','E','F','G'],
    ['Z','a','a','b','b','H','U','U','T'],
    ['Z','a','Y','b','e','e','V','U','T'],
    ['Z','Y','Y','d','d','d','V','V','S'],
    ['W','X','Y','c','c','Q','V','R','S'],
    ['W','X','X','P','Q','Q','R','R','S'],
    ['K','L','M','P','N','O','I','I','J'],
    ['K','L','M','N','N','O','I','I','J']])
test_killer_4_sums = {
    'A': 6, 'B': 16, 'C': 14, 'D': 15, 
    'E': 8, 'F': 7, 'G': 17, 'H': 10, 'I': 25, 
    'J': 7, 'K': 13, 'L': 12, 'M': 5, 'N': 14, 
    'O': 11, 'P': 9, 'Q': 17, 'R': 12, 'S': 16, 
    'T': 5, 'U': 21, 'V': 17, 'W': 12, 'X': 15, 
    'Y': 27, 'Z': 14, 'a': 15, 'b': 13, 'c': 10, 
    'd': 15, 'e': 7}

test_killer_5_matrix= np.array([
    ['A','B','C','D','D','F','F','H','I'],
    ['A','B','C','E','E','G','G','H','I'],
    ['J','B','Y','Y','f','f','U','U','T'],
    ['J','J','h','g','d','e','V','V','T'],
    ['X','a','h','g','d','e','W','V','S'],
    ['X','a','Z','c','d','b','W','R','S'],
    ['K','Z','Z','c','b','b','P','R','Q'],
    ['K','K','M','M','O','O','P','L','Q'],
    ['K','K','M','M','N','N','L','L','L']])
test_killer_5_sums = {
    'A': 5, 'B': 18, 'C': 17, 'D': 14, 
    'E': 16, 'F': 11, 'G': 6, 'H': 6, 'I': 4, 
    'J': 12, 'K': 27, 'L': 25, 'M': 18, 'N': 15, 
    'O': 7, 'P': 3, 'Q': 10, 'R': 10, 'S': 16, 
    'T': 10, 'U': 15, 'V': 12, 'W': 12, 'X': 9, 
    'Y': 6, 'Z': 17, 'a': 11, 'b': 12, 'c': 5, 
    'd': 13, 'e': 16, 'f': 5, 'g': 9, 'h': 13}

test_killer_6_matrix = np.array([
        ['A','B','C','C','C','D','D','E','F'],
        ['A','B','Y','Y','X','X','G','E','F'],
        ['Z','b','b','d','d','W','G','H','H'],
        ['Z','c','e','h','h','W','S','S','R'],
        ['a','c','e','g','h','V','T','T','R'],
        ['a','c','f','g','N','V','U','R','R'],
        ['I','I','f','K','N','V','U','P','Q'],
        ['I','I','K','K','N','O','O','P','Q'],
        ['L','L','K','K','M','M','J','J','J']])
test_killer_6_sums = {
    'A': 7, 'B': 13, 'C': 11, 'D': 6, 
    'E': 9, 'F': 15, 'G': 13, 'H': 7, 'I': 16, 
    'J': 16, 'K': 29, 'L': 8, 'M': 7, 'N': 21, 
    'O': 14, 'P': 11, 'Q': 5, 'R': 18, 'S': 15, 
    'T': 9, 'U': 10, 'V': 14, 'W': 5, 'X': 13, 
    'Y': 8, 'Z': 16, 'a': 10, 'b': 7, 'c': 14, 
    'd': 15, 'e': 8, 'f': 15, 'g': 13, 'h': 7}

test_killer_7_matrix = np.array([
    ['A','A','D','D','W','X','X','U','V'],
    ['B','B','E','E','W','Y','Y','U','V'],
    ['C','C','F','F','g','g','Y','T','T'],
    ['H','C','G','G','f','f','Z','S','S'],
    ['H','c','c','e','e','f','Z','R','R'],
    ['I','I','c','d','d','Z','Z','Q','R'],
    ['J','J','L','b','a','P','P','Q','O'],
    ['K','L','L','b','a','P','P','P','O'],
    ['K','M','M','M','M','N','N','O','O']])
test_killer_7_sums = {
    'A': 12, 'B': 3, 'C': 9, 'D': 14, 
    'E': 17, 'F': 13, 'G': 6, 'H': 10, 'I': 14, 
    'J': 13, 'K': 9, 'L': 14, 'M': 19, 'N': 11, 
    'O': 20, 'P': 26, 'Q': 6, 'R': 20, 'S': 11, 
    'T': 14, 'U': 7, 'V': 9, 'W': 7, 'X': 12, 
    'Y': 17, 'Z': 19, 'a': 10, 'b': 9, 'c': 14, 
    'd': 14, 'e': 8, 'f': 15, 'g': 3}

test_killer_8_matrix = np.array([
    ['A','B','B','C','D','E','F','F','F'],
    ['A','B','B','C','D','E','G','H','H'],
    ['A','L','L','M','O','G','G','J','I'],
    ['K','N','M','M','O','P','P','J','I'],
    ['K','N','b','g','g','R','Q','I','I'],
    ['Z','a','b','e','f','R','Q','S','S'],
    ['Z','a','Y','e','f','V','V','T','U'],
    ['X','X','Y','d','d','V','V','T','U'],
    ['W','W','Y','c','c','V','V','U','U']])
test_killer_8_sums = {
    'A': 24, 'B': 12, 'C': 9, 'D': 13, 
    'E': 12, 'F': 16, 'G': 7, 'H': 10, 'I': 19, 
    'J': 9, 'K': 4, 'L': 9, 'M': 8, 'N': 13, 
    'O': 15, 'P': 15, 'Q': 12, 'R': 9, 'S': 13, 
    'T': 4, 'U': 21, 'V': 33, 'W': 9, 'X': 5, 
    'Y': 16, 'Z': 10, 'a': 16, 'b': 15, 'c': 10, 
    'd': 14, 'e': 9, 'f': 7, 'g': 7}

#67 second setup 245 second solve
test_killer_9_matrix = np.array([
                        ['A','A','B','B','B','B','B','C','C'],
                        ['D','E','E','G','H','J','I','I','L'],
                        ['D','F','F','G','H','J','K','K','L'],
                        ['D','D','M','M','M','M','M','L','L'],
                        ['X','X','Y','Y','M','R','R','Q','Q'],
                        ['X','W','W','W','T','P','P','P','Q'],
                        ['W','W','N','T','T','T','O','P','P'],
                        ['W','N','N','V','U','S','O','O','P'],
                        ['N','N','V','V','U','S','S','O','O']])
test_killer_9_sums = {
                    'A': 12, 'B': 25, 'C': 8, 'D': 15, 
                    'E': 9, 'F': 9, 'G': 14, 'H': 7, 'I': 12, 
                    'J': 14, 'K': 16, 'L': 12, 'M': 33, 'N': 27, 
                    'O': 29, 'P': 27, 'Q': 20, 'R': 5, 'S': 8, 
                    'T': 21, 'U': 16, 'V': 14, 'W': 25, 'X': 20, 
                    'Y': 7}

test_killer_10_matrix = np.array([
    ['A','A','A','C','D','E','E','F','F'],
    ['A','A','A','C','D','U','U','F','N'],
    ['A','A','B','B','U','U','V','V','N'],
    ['T','T','B','X','X','W','W','V','M'],
    ['S','S','R','X','Y','Y','W','O','M'],
    ['Q','R','R','Z','Y','Y','P','O','M'],
    ['Q','R','L','Z','Z','P','P','O','M'],
    ['H','H','L','L','K','K','K','G','G'],
    ['H','I','I','J','J','J','J','G','G']])
test_killer_10_sums = {
    'A': 42, 'B': 20, 'C': 13, 'D': 5, 
    'E': 12, 'F': 16, 'G': 14, 'H': 20, 'I': 10, 
    'J': 19, 'K': 18, 'L': 13, 'M': 20, 'N': 10, 
    'O': 24, 'P': 18, 'Q': 7, 'R': 17, 'S': 7, 
    'T': 8, 'U': 19, 'V': 11, 'W': 12, 'X': 22, 
    'Y': 18, 'Z': 10}

#Exact Cover Problems
print('--------------------------------------------------------------')
print('-------------------EXACT COVER PROBLEMS-----------------------')

with Timer("test 1 (exact cover): setting up"):
    test_1 = exact_cover.Exact_Cover(test_matrix_1)

print(test_matrix_1)

with Timer("test 1 (exact cover): solving"):
    algorithm_dlx.AlgorithmDLX(test_1, 'exact cover')

print('--------------------------------------------------------------')

with Timer("test 2 (exact cover): setting up"):
    test_2 = exact_cover.Exact_Cover(test_matrix_2)

print(test_matrix_2)

with Timer("test 2 (exact cover): solving"):
    algorithm_dlx.AlgorithmDLX(test_2, 'exact cover')

print('--------------------------------------------------------------')

with Timer("test 3 (exact cover): setting up"):
    test_3 = exact_cover.Exact_Cover(test_matrix_3)

print(test_matrix_3)

with Timer("test 3 (exact cover): solving"):
    algorithm_dlx.AlgorithmDLX(test_3, 'exact cover')   

print('--------------------------------------------------------------')

with Timer("test 4 (exact cover): setting up"):
    test_4 = exact_cover.Exact_Cover(test_matrix_4)

print(test_matrix_4)

with Timer("test 4 (exact cover): solving"):
    algorithm_dlx.AlgorithmDLX(test_4, 'exact cover') 

print('--------------------------------------------------------------')

with Timer("test 5 (exact cover): setting up"):
    test_5 = exact_cover.Exact_Cover(test_matrix_5)

print(test_matrix_5)

with Timer("test 5 (exact cover): solving"):
    algorithm_dlx.AlgorithmDLX(test_5, 'exact cover')

print('--------------------------------------------------------------')
print('----------------------SUDOKU PROBLEMS-------------------------')
print('\nThere are 10 example Sudokus included here. The difficulty in-')
print('creases with every few puzzles, however this has almost no im-')
print('pact on the solve times.')
with Timer("test 1 (sudoku): setting up"):
    test_1 = sudoku.Sudoku(test_sudoku_1)

print(test_sudoku_1)

with Timer("test 1 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_1, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 2 (sudoku): setting up"):
    test_2 = sudoku.Sudoku(test_sudoku_2)

print(test_sudoku_2)

with Timer("test 2 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_2, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 3 (sudoku): setting up"):
    test_3 = sudoku.Sudoku(test_sudoku_3)

print(test_sudoku_3)

with Timer("test 3 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_3, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 4 (sudoku): setting up"):
    test_4 = sudoku.Sudoku(test_sudoku_4)

print(test_sudoku_4)

with Timer("test 4 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_4, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 5 (sudoku): setting up"):
    test_5 = sudoku.Sudoku(test_sudoku_5)

print(test_sudoku_5)

with Timer("test 5 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_5, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 6 (sudoku): setting up"):
    test_6 = sudoku.Sudoku(test_sudoku_6)

print(test_sudoku_6)

with Timer("test 6 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_6, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 7 (sudoku): setting up"):
    test_7 = sudoku.Sudoku(test_sudoku_7)

print(test_sudoku_7)

with Timer("test 7 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_7, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 8 (sudoku): setting up"):
    test_8 = sudoku.Sudoku(test_sudoku_8)

print(test_sudoku_8)

with Timer("test 8 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_8, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 9 (sudoku): setting up"):
    test_9 = sudoku.Sudoku(test_sudoku_9)

print(test_sudoku_9)

with Timer("test 9 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_9, 'sudoku')

print('--------------------------------------------------------------')

with Timer("test 10 (sudoku): setting up"):
    test_10 = sudoku.Sudoku(test_sudoku_10)

print(test_sudoku_10)

with Timer("test 10 (sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_10, 'sudoku')

print('--------------------------------------------------------------')
print('-----------------KILLER SUDOKU PROBLEMS-----------------------')
print('\nThere are 10 example Killer Sudoku included here. The difficu-')
print('lty increases with every few puzzles. The last two puzzles are ')
print('"extreme"  and  "mind-bending" difficulty, and as such take a ')
print('long time to solve, exhibiting the limitations of the  solver ')
print('when multiple large cage sizes are involved.')


with Timer("test 1 (killer sudoku): setting up"):
    test_1 = killer.Killer_Sudoku(test_killer_1_matrix, test_killer_1_sums)

with Timer("test 1 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_1, 'killer')

print('--------------------------------------------------------------')

with Timer("test 2 (killer sudoku): setting up"):
    test_2 = killer.Killer_Sudoku(test_killer_2_matrix, test_killer_2_sums)

with Timer("test 2 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_2, 'killer')

print('--------------------------------------------------------------')

with Timer("test 3 (killer sudoku): setting up"):
    test_3 = killer.Killer_Sudoku(test_killer_3_matrix, test_killer_3_sums)

with Timer("test 3 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_3, 'killer')

print('--------------------------------------------------------------')

with Timer("test 4 (killer sudoku): setting up"):
    test_4 = killer.Killer_Sudoku(test_killer_4_matrix, test_killer_4_sums)

with Timer("test 4 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_4, 'killer')
    
print('--------------------------------------------------------------')

with Timer("test 5 (killer sudoku): setting up"):
    test_5 = killer.Killer_Sudoku(test_killer_5_matrix, test_killer_5_sums)

with Timer("test 5 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_5, 'killer')
    
print('--------------------------------------------------------------')

with Timer("test 6 (killer sudoku): setting up"):
    test_6 = killer.Killer_Sudoku(test_killer_6_matrix, test_killer_6_sums)

with Timer("test 6 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_6, 'killer')
    
print('--------------------------------------------------------------')

with Timer("test 7 (killer sudoku): setting up"):
    test_7 = killer.Killer_Sudoku(test_killer_7_matrix, test_killer_7_sums)

with Timer("test 7 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_7, 'killer')
    
print('--------------------------------------------------------------')

with Timer("test 8 (killer sudoku): setting up"):
    test_8 = killer.Killer_Sudoku(test_killer_8_matrix, test_killer_8_sums)

with Timer("test 8 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_8, 'killer')
    
print('--------------------------------------------------------------')

with Timer("test 9 (killer sudoku): setting up"):
    test_9 = killer.Killer_Sudoku(test_killer_9_matrix, test_killer_9_sums)

with Timer("test 9 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_9, 'killer')
    
print('--------------------------------------------------------------')

with Timer("test 10 (killer sudoku): setting up"):
    test_10 = killer.Killer_Sudoku(test_killer_10_matrix, test_killer_10_sums)

with Timer("test 10 (killer sudoku): solving"):
    algorithm_dlx.AlgorithmDLX(test_10, 'killer')
    
print('--------------------------------------------------------------')


