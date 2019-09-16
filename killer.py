import dlx
import numpy as np 
import itertools as it 
import time

#characters represent a cage


class Cage():
    """
    Object representing a cage, or clue in killer sudoku

    Attributes:
        - sum, int, number that cells in cage must sum to
        - size, int, number of cells in cage
        - coords, list, coordinates of cage cells in sudoku puzzle stored as tuples
        - candidates, list, all possible combinations of numbers that could be placed in cage satisfying size and sum
        - ncandidates, int, number of candidates
    """

    def __init__(self, cage_sum):
        self.sum = cage_sum
        self.size = 0
        self.coords = []
        self.candidates = None
        self.ncandidates = None

class Killer_Sudoku():
    """
    Constructs a dancing links matrix based off a killer sudoku puzzle for use in algorithmX

    Attributes:
        - input_matrix, nparray, matrix containing killer cages 
        - input_sums, dictionary, contains cage sums 
        - dlmatrix, dictionary, contains the Nodes and Headers that form the dancing links matrix
        - counter, int, running counter of objects created in dlmatrix 
        - cages, dictionary, contains cage objects
        - noptions, integer, number of options created
        - headers_ref, list, reference numbers of headers
        - spacers_ref, list, reference numbers of spacers
        - nodes_ref, list, lists of node reference numbers for each option
        - options_ref, dictionary, contains reference for each option to the sudoku move it represents

    Methods:
        - generate_sums(), generates sums for cage permutations
        - generate_cages(), creates cages
        - create_headers(), creates Header objects
        - create_nodes(), creates Node and spacer Node objects
        - create_links(), links all objects created by create_headers and crate_nodes
        - create_dlmatrix(), creates dlmatrix
        - display_cage_info(), displays cage information
        - cage_constraints(), iterates through cells in a cage calling move_constraint()
        - move_constraint(), returns constraint numbers satisfied by move
        - output_solution(), formats the solution returned from algorithmX into a solved killer sudoku grid
        - display_info(), displays information about the dlmatrix
    """

    def __init__(self, input_matrix, input_sums):
        self.input_matrix = input_matrix
        self.input_sums = input_sums

        self.dlmatrix = {}
        self.counter = 0

        self.cages = {}
        self.noptions = 0
        self.headers_ref = []
        self.spacers_ref = []
        self.nodes_ref = []
        self.options_ref = {}
        self.create_dlmatrix()

    def generate_sums(self, cage_sum, size):
        """returns all permutations of size 'size' that sum to 'value' as a list of tuples"""
        #only the numbers 1-9 can be used as usual for sudoku
        numbers = [1,2,3,4,5,6,7,8,9]
        output_sums = []
        all_combinations = list(it.permutations(numbers, size))
        for combination in range(len(all_combinations)):
            if sum(all_combinations[combination]) == cage_sum:
                output_sums.append(all_combinations[combination])
        #the output is a list of tuples, where each tuple is a candidate
        return output_sums        

    def generate_cages(self):
        """generates a Cage object for each cage in the given problem"""
        for cage_ref, cage in self.input_sums.items():
            self.cages[cage_ref] = Cage(cage)

        for row in range(self.input_matrix.shape[0]):
            for col in range(self.input_matrix.shape[1]):
                self.cages[self.input_matrix[row][col]].coords.append((row, col))
                self.cages[self.input_matrix[row][col]].size += 1

        for cage_ref, cage in self.input_sums.items():
            cage_candidates = self.generate_sums(cage, self.cages[cage_ref].size)
            self.cages[cage_ref].candidates = cage_candidates
            self.noptions += len(cage_candidates)
            self.cages[cage_ref].ncandidates = len(self.cages[cage_ref].candidates)

    def create_headers(self):
        """Creates Header objects for each of the 324 items (constraints) plus a Header zero"""
        while self.counter < (324+1):
            self.dlmatrix[self.counter] = dlx.Header(self.counter)
            self.headers_ref.append(self.counter)
            self.counter += 1

    def create_nodes(self):
        """Creates Node and spacer Node objects according to constraint matrix for killer sudoku problem"""
        option_counter = 0
        #create first spacer
        self.dlmatrix[self.counter] = dlx.Node(None, len(self.spacers_ref)*-1, self.counter)
        self.spacers_ref.append(self.counter)
        self.counter += 1

        for cage_ref in self.cages.keys():
            for option in range(len(self.cages[cage_ref].candidates)):
                new_option = self.cage_constraints(self.cages[cage_ref].candidates[option], self.cages[cage_ref].coords)
                self.options_ref[option_counter] = (self.cages[cage_ref].candidates[option], self.cages[cage_ref].coords)
                self.nodes_ref.append([])
                for node in new_option:
                    self.dlmatrix[self.counter] = dlx.Node(option_counter, node, self.counter) 
                    self.nodes_ref[-1].append(self.counter)
                    self.counter += 1
                #create every other spacer
                self.dlmatrix[self.counter] = dlx.Node(None, len(self.spacers_ref)*-1, self.counter)
                self.spacers_ref.append(self.counter)
                self.counter += 1

                option_counter +=1
        
    def create_links(self):
        """Create every link in the dlmatrix"""
        ref_lists = []
        for item in range(1, len(self.headers_ref)+1):
            ref_lists.append([])
        for item in range(len(ref_lists)):
            ref_lists[item].append(self.headers_ref[item])
            for option in range(len(self.nodes_ref)):
                for node in range(len(self.nodes_ref[option])):
                    if self.dlmatrix[self.nodes_ref[option][node]].top == item:
                        ref_lists[item].append(self.nodes_ref[option][node])

        #first set len of headers
        for header in self.headers_ref:
            self.dlmatrix[header].len = len(ref_lists[header])-1

        #next link headers
        for item in range(len(self.headers_ref)):
            if item == 0:
                self.dlmatrix[self.headers_ref[item]].left = self.dlmatrix[self.headers_ref[-1]]
                self.dlmatrix[self.headers_ref[item]].right = self.dlmatrix[self.headers_ref[item+1]]
            elif item == len(self.headers_ref)-1:
                self.dlmatrix[self.headers_ref[item]].right = self.dlmatrix[self.headers_ref[0]]
                self.dlmatrix[self.headers_ref[item]].left = self.dlmatrix[self.headers_ref[item-1]]
                self.dlmatrix[self.headers_ref[item]].below = self.dlmatrix[ref_lists[item][1]]
                self.dlmatrix[self.headers_ref[item]].above = self.dlmatrix[ref_lists[item][-1]]
            else:
                self.dlmatrix[self.headers_ref[item]].left = self.dlmatrix[self.headers_ref[item-1]]
                self.dlmatrix[self.headers_ref[item]].right = self.dlmatrix[self.headers_ref[item+1]]
                self.dlmatrix[self.headers_ref[item]].below = self.dlmatrix[ref_lists[item][1]]
                self.dlmatrix[self.headers_ref[item]].above = self.dlmatrix[ref_lists[item][-1]]
      
        #next nodes
        for item in range(len(ref_lists)):
            for node in range(1, len(ref_lists[item])):
                if node == len(ref_lists[item])-1:
                    self.dlmatrix[ref_lists[item][node]].below = self.dlmatrix[ref_lists[item][0]]
                    self.dlmatrix[ref_lists[item][node]].above = self.dlmatrix[ref_lists[item][node-1]]
                elif node == 0:
                    self.dlmatrix[ref_lists[item][node]].below = self.dlmatrix[ref_lists[item][node+1]]
                    self.dlmatrix[ref_lists[item][node]].above = self.dlmatrix[ref_lists[item][-1]]
                else:
                    self.dlmatrix[ref_lists[item][node]].below = self.dlmatrix[ref_lists[item][node+1]]
                    self.dlmatrix[ref_lists[item][node]].above = self.dlmatrix[ref_lists[item][node-1]]

        #finally link spacers
        for spacer in range(len(self.spacers_ref)):
            if spacer == 0:
                self.dlmatrix[self.spacers_ref[spacer]].below = self.dlmatrix[self.nodes_ref[spacer][-1]]
            elif spacer == (len(self.spacers_ref)-1):
                self.dlmatrix[self.spacers_ref[spacer]].above = self.dlmatrix[self.nodes_ref[spacer-1][0]]
            else:
                self.dlmatrix[self.spacers_ref[spacer]].above = self.dlmatrix[self.nodes_ref[spacer-1][0]]
                self.dlmatrix[self.spacers_ref[spacer]].below = self.dlmatrix[self.nodes_ref[spacer][-1]]

    def create_dlmatrix(self):
        self.generate_cages()
        self.create_headers()
        self.create_nodes()
        self.create_links()
        print(str(len(self.headers_ref)) + ' items')
        print(str(len(self.nodes_ref)) + ' options')

    def display_cage_info(self, cage):
        """Prints info about cage"""
        print('\ncage: ' + cage )
        print('sum: ' + str(self.cages[cage].sum))
        print('size: ' + str(self.cages[cage].size))
        print('coords: ' + str(self.cages[cage].coords))
        print('there are ' + str(self.cages[cage].ncandidates) + ' candidates: \n')
        print(str(self.cages[cage].candidates))

    def cage_constraints(self, cage_candidate, cage_coords):
        """Finds the constraints satisfied by a cage candidate (option)"""
        cage_constraints = []
        for cell in range(len(cage_candidate)):
            cell_constraints = self.move_constraint(cage_candidate[cell], cage_coords[cell])
            cage_constraints += cell_constraints
        
        return cage_constraints

    def move_constraint(self, cell_candidate, cell_coords):
        """Takes a move i.e a number in a cell and returns the constraints it satisfies"""
        #first calculate cell constraint
        cell_constraint = (cell_coords[0]*9)+1 + cell_coords[1]
        #next row constraint
        row_constraint = 81 + cell_candidate + (cell_coords[0]*9)
        #next column constraint
        column_constraint = 162 + cell_candidate + (cell_coords[1]*9)
        #finally block constraint
        if cell_coords[0] < 3 and cell_coords[1] < 3:
            block_constraint = 243 + cell_candidate
        elif cell_coords[0] < 3 and 3 <= cell_coords[1] < 6:
            block_constraint = 252 + cell_candidate
        elif cell_coords[0] < 3 and 6 <= cell_coords[1] < 9:
            block_constraint = 261 + cell_candidate
        elif 3 <= cell_coords[0] < 6 and cell_coords[1] < 3:
            block_constraint = 270 + cell_candidate
        elif 3 <= cell_coords[0] < 6 and 3 <= cell_coords[1] < 6:
            block_constraint = 279 + cell_candidate
        elif 3 <= cell_coords[0]< 6 and 6 <= cell_coords[1] < 9:
            block_constraint = 288 + cell_candidate
        elif 6 <= cell_coords[0] and cell_coords[1] < 3:
            block_constraint = 297 + cell_candidate
        elif 6 <= cell_coords[0] and 3 <= cell_coords[1] < 6:
            block_constraint = 306 + cell_candidate
        elif 6 <= cell_coords[0] and 6 <= cell_coords[1] < 9:
            block_constraint = 315 + cell_candidate

        move_constraints = [cell_constraint, row_constraint, column_constraint, block_constraint]

        return move_constraints

    def output_solution(self, solution):
        solved_grid = np.array([
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]])
        
        for option in solution:
            for cage_size in range(len(self.options_ref[option][1])):
                solved_grid[self.options_ref[option][1][cage_size][0]][self.options_ref[option][1][cage_size][1]] = self.options_ref[option][0][cage_size]
        print(solved_grid)

    def display_info(self, object_number = None):
        """Displays object information, if no object is specified displays all objects information"""
        if object_number == None:
            for dlmatrix_object in range(self.counter):
                if dlmatrix_object == 0:
                    print('\nheader ' + str(self.dlmatrix[dlmatrix_object].number) + ' has len ' + str(self.dlmatrix[dlmatrix_object].len) +' and links ' )
                    print('left ' + str(self.dlmatrix[dlmatrix_object].left.number))
                    print('right ' + str(self.dlmatrix[dlmatrix_object].right.number))
                elif dlmatrix_object in self.headers_ref and dlmatrix_object != 0:
                    print('\nheader ' + str(self.dlmatrix[dlmatrix_object].number) + ' has len ' + str(self.dlmatrix[dlmatrix_object].len) +' and links ' )
                    print('left ' + str(self.dlmatrix[dlmatrix_object].left.number))
                    print('right ' + str(self.dlmatrix[dlmatrix_object].right.number))
                    print('above ' + str(self.dlmatrix[dlmatrix_object].above.number))
                    print('below ' + str(self.dlmatrix[dlmatrix_object].below.number))
                elif dlmatrix_object in self.spacers_ref:
                    if dlmatrix_object == self.spacers_ref[0]:
                        print('\nspacer ' + str(self.dlmatrix[dlmatrix_object].number) + ' has top ' + str(self.dlmatrix[dlmatrix_object].top) + ' and links ')
                        print('below ' + str(self.dlmatrix[dlmatrix_object].below.number))
                    elif dlmatrix_object == self.spacers_ref[-1]:
                        print('\nspacer ' + str(self.dlmatrix[dlmatrix_object].number) + ' has top ' + str(self.dlmatrix[dlmatrix_object].top) + ' and links ')
                        print('above ' + str(self.dlmatrix[dlmatrix_object].above.number))                    
                    else:
                        print('\nspacer ' + str(self.dlmatrix[dlmatrix_object].number) + ' has top ' + str(self.dlmatrix[dlmatrix_object].top) + ' and links ')
                        print('above ' + str(self.dlmatrix[dlmatrix_object].above.number))
                        print('below ' + str(self.dlmatrix[dlmatrix_object].below.number))
                else:
                    print('\nnode ' + str(self.dlmatrix[dlmatrix_object].number) + ' has top ' + str(self.dlmatrix[dlmatrix_object].top) + ' and links ')
                    print('above ' + str(self.dlmatrix[dlmatrix_object].above.number))
                    print('below ' + str(self.dlmatrix[dlmatrix_object].below.number))
        else:
            if object_number == 0:
                print('\nheader ' + str(self.dlmatrix[object_number].number) + ' has len ' + str(self.dlmatrix[object_number].len) +' and links ' )
                print('left ' + str(self.dlmatrix[object_number].left.number))
                print('right ' + str(self.dlmatrix[object_number].right.number))
            elif object_number in self.headers_ref and object_number != 0:
                print('\nheader ' + str(self.dlmatrix[object_number].number) + ' has len ' + str(self.dlmatrix[object_number].len) +' and links ' )
                print('left ' + str(self.dlmatrix[object_number].left.number))
                print('right ' + str(self.dlmatrix[object_number].right.number))
                print('above ' + str(self.dlmatrix[object_number].above.number))
                print('below ' + str(self.dlmatrix[object_number].below.number))
            elif object_number in self.spacers_ref:
                print('\nspacer ' + str(self.dlmatrix[object_number].number) + ' has top ' + str(self.dlmatrix[object_number].top) + ' and links ')
                print('above ' + str(self.dlmatrix[object_number].above.number))
                print('below ' + str(self.dlmatrix[object_number].below.number))
            else:
                print('\nnode ' + str(self.dlmatrix[object_number].number) + ' has top ' + str(self.dlmatrix[object_number].top) + ' and links ')
                print('above ' + str(self.dlmatrix[object_number].above.number))
                print('below ' + str(self.dlmatrix[object_number].below.number))
