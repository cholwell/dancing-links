import dlx
import numpy as np

class Sudoku():
    """
    Constructs a dancing links matrix from a sudoku puzzle, for use in algorithmX

    Attributes:
        - input_matrix, nparray, matrix containing partial sudoku to be solved
        - dlmatrix, dictionary, contains the Nodes and Headers that form the dancing links matrix
        - counter, int, running counter of objects created in dlmatrix 
        - headers_ref, list, reference numbers of headers
        - spacers_ref, list, reference numbers of spacers
        - nodes_ref, list, lists of node reference numbers for each option
        - options_ref, dictionary, contains reference for each option to the sudoku move it represents
        - clues, list, list of clues from partial solution
        - partial_solution, list, list of options corresponding to the clues from partial solution

    Methods:
        - create_headers(), creates Header objects
        - create_nodes(), creates Node and spacer Node objects
        - create_links(), links all objects created by create_headers and crate_nodes
        - create_dlmatrix(), creates dlmatrix
        - option_lookup(), returns a move in sudoku based off option argument
        - create_options_ref(), creates a dictionary containing all option - move pairs
        - list_clues(), creates a list of options based off partial solution
        - output_solution(), formats the solution returned from algorithmX into a solved sudoku grid
        - display_info(), displays information about the dlmatrix
    """
    def __init__(self, input_matrix):
        self.input_matrix = np.copy(input_matrix)
        self.dlmatrix = {}
        self.counter = 0
        self.headers_ref = []
        self.spacers_ref = []
        self.nodes_ref = [[] for option in range(729)]
        self.options_ref = {}
        self.clues = []
        self.partial_solution = []
        
        #create dlmatrix when class is called
        self.create_dlmatrix()

    def create_headers(self):
        """Creates Header object for each of the 324 items (constraints) plus a Header zero"""
        #create a Header object in self.dlmatrix with Header number attribute as key
        while self.counter < (324+1):
            self.dlmatrix[self.counter] = dlx.Header(self.counter)
            self.dlmatrix[self.counter].len = 9
            self.headers_ref.append(self.counter)
            self.counter +=1

    def create_nodes(self):
        """Create Node and spacer Node objects according to constraint matrix for sudoku"""
        #Nodes and spacer Nodes are created sequentially
        self.dlmatrix[self.counter] = dlx.Node(None, len(self.spacers_ref)*-1, self.counter)
        self.spacers_ref.append(self.counter)
        self.counter += 1
        for option in range(len(self.nodes_ref)):
            node_iter = 0
            while node_iter < 4:
                self.dlmatrix[self.counter] = dlx.Node(option, None, self.counter)
                self.nodes_ref[option].append(self.counter)
                self.counter += 1
                node_iter += 1
            self.dlmatrix[self.counter] = dlx.Node(None, len(self.spacers_ref)*-1, self.counter)
            self.spacers_ref.append(self.counter)
            self.counter += 1
        
        #Specify the correct top attribute for the non spacer Nodes just created
        #cell constraints
        for constraint in range(81):
            for option in range(9):
                self.dlmatrix[self.nodes_ref[constraint*9+option][0]].top = constraint + 1

        #row constraints
        row_constraints_iter = 0
        row_constraints_start = 82
        for constraint in range(81):
            for option in range(9):
                self.dlmatrix[self.nodes_ref[constraint*9+option][1]].top = row_constraints_start+option
            row_constraints_iter += 1
            if row_constraints_iter % 9 == 0:
                row_constraints_start += 9

        #column constraints
        column_constraints_start = 163
        for constraint in range(81):
            for option in range(9):
                self.dlmatrix[self.nodes_ref[constraint*9+option][2]].top = column_constraints_start
                column_constraints_start += 1
                if column_constraints_start == 244:
                    column_constraints_start = 163

        block_constraints_iter = 0
        block_constraints_start = 244
        for constraint in range(81):
            for option in range(9):
                self.dlmatrix[self.nodes_ref[constraint*9+option][3]].top = block_constraints_start + option
            
            block_constraints_iter += 1
            if block_constraints_iter % 3 == 0:
                block_constraints_start += 9
            
            if block_constraints_iter == 9 or block_constraints_iter == 18:
                block_constraints_start = 244
            
            if block_constraints_iter == 27 or block_constraints_iter == 36 or block_constraints_iter == 45:
                block_constraints_start = 271
            
            if block_constraints_iter == 54 or block_constraints_iter == 63 or block_constraints_iter == 72:
                block_constraints_start = 298

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

        #first link headers
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
            #print('item is ' + str(item) + ' with vertical list ')
            #print(ref_list_vert[item])
            for node in range(1, len(ref_lists[item])):
                #print('node is ' + str( self.dlmatrix[ref_list_vert[item][node]).number) + ' with loop number ' + str(node))
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
        """Creates dlmatrix"""
        self.create_headers()
        self.create_nodes()
        self.create_links()
        self.create_options_ref()
        self.list_clues()
        
    def option_lookup(self, option):
        """returns the location and value of a move in sudoku based off the option from the constraint matrix"""
        output_row = 1
        output_column = 1
        output_value = 1
        for iter in range(1,option+1):
            output_value +=1
            if output_value == 10:
                output_value = 1
            if iter > 8 and iter % 9 == 0:
                output_column +=1
                if output_column == 10:
                    output_column = 1
            if iter > 80 and iter % 81 == 0:
                output_row +=1
                
        output = [output_row, output_column, output_value]
        return output

    def create_options_ref(self):
        """calls option_lookup to create a dictionary of options and corresponding sudoku moves"""
        for option in range(729):
            self.options_ref[option] = self.option_lookup(option)
            self.options_ref[str(self.option_lookup(option))] = option

    def list_clues(self):
        """Create a list of options that must be included in the solution based off partial sudoku provided"""
        for row in range(self.input_matrix.shape[0]):
            for col in range(self.input_matrix.shape[1]):
                if self.input_matrix[row][col] != 0:
                    clue = str([row+1, col+1, self.input_matrix[row][col]])
                    self.clues.append(self.options_ref[clue])

        for clue in range(len(self.clues)):
            for node in range(4):
                if self.dlmatrix[self.nodes_ref[self.clues[clue]][node]].top not in self.partial_solution:
                    self.partial_solution.append(self.dlmatrix[self.nodes_ref[self.clues[clue]][node]].top)

    def output_solution(self, solution, return_method = 'print'):
        """Takes a list of options from algorithmX output and prints the solved sudoku grid"""
        solved_grid = self.input_matrix

        for entry in range(len(solution)):
            input_entry = solution[entry]
            grid_input = self.options_ref[input_entry]
            solved_grid[grid_input[0]-1][grid_input[1]-1] = grid_input[2]

        if return_method == 'print':
            print('\n')
            print(solved_grid)
        elif return_method == 'savetxt': 
            np.savetxt('trial.txt', solved_grid, fmt='%i')

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
