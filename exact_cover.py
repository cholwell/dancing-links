import dlx

class Exact_Cover():
    """
    Constructs a dancing links matrix from a matrix representing an exact cover problem for use
    in AlgorithmX

    Attributes:
        - input_matrix, nparray,  matrix representing exact cover problem to be solved
        - options, int, number of options in exact cover problem
        - items, int, number of items in exact cover problem
        - dlmatrix, dictionary, contains the Nodes and Headers that form the dancing links matrix
        - counter, int, running counter of objects created in dlmatrix
        - headers_ref, list, reference numbers of headers
        - spacers_ref, list, reference numbers of spacers
        - nodes_ref, list, lists of node reference numbers for each option

    Methods:
        - create_headers(), creates Header objects
        - create_nodes(), creates Node and spacer Node objects
        - create_links(), links all objects created by create_headers() and create_nodes() 
        - create_dlmatrix(), creates dlmatrix
        - output_solution(), formats solution returned from AlgorithmX
        - display_info(), prints information about the dlmatrix
    """
    def __init__(self, input_matrix):
        self.input_matrix = input_matrix
        self.options = input_matrix.shape[0]
        self.items = input_matrix.shape[1]
        self.dlmatrix = {}
        self.counter = 0
        self.headers_ref = []
        self.spacers_ref = []
        self.nodes_ref = [[] for option in range(self.options)]

        #create dlmatrix when class is called
        self.create_dlmatrix()

    def create_headers(self):
        """Creates Header objects for every item plus a Header zero"""
        #create a Header object in self.dlmatrix with Header number attribute as key
        while self.counter < (self.items+1):
            self.dlmatrix[self.counter] = dlx.Header(self.counter)
            self.headers_ref.append(self.counter)
            self.counter += 1
            
        #for each Header except zero Header, set len attribute 
        for col in range(self.items):
            for row in range(self.options):
                if self.input_matrix[row, col] == 1:
                    self.dlmatrix[(col+1)].len += 1
    
    def create_nodes(self):
        """Create a Node in dlmatrix for each 1 in input_matrix with number as key.
        Create a spacer Node in dlmatrix for each option with number as key"""
        #Nodes and spacer Nodes are created sequentially 
        for row in range(self.options):
            #create spacer Node
            self.dlmatrix[self.counter] = dlx.Node(None, (len(self.spacers_ref)*-1), self.counter)
            self.spacers_ref.append(self.counter)
            self.counter += 1
            for col in range(self.items):
                #create Node
                if self.input_matrix[row, col] == 1:
                    self.dlmatrix[self.counter] = dlx.Node(row, col+1, self.counter)
                    self.nodes_ref[row].append(self.counter)
                    self.counter += 1

        #create final spacer Node
        self.dlmatrix[self.counter] = dlx.Node(None, (len(self.spacers_ref)*-1), self.counter)
        self.spacers_ref.append(self.counter)
        self.counter += 1

    def create_links(self):
        """Creates every link in the dlmatrix"""
        #create reference list for vertical links
        ref_lists = []
        for item in range(1, len(self.headers_ref)):
            ref_lists.append([])    
            ref_lists[item-1].append(item)
        
        for ref_list in range(len(ref_lists)):
            for node in range(len(self.headers_ref), self.counter):
                if self.dlmatrix[node].top == ref_lists[ref_list][0]:
                    ref_lists[ref_list].append(self.dlmatrix[node].number)
        
        #link headers
        for item in range(self.items+1):
            if item == 0:
                self.dlmatrix[item].left = self.dlmatrix[self.items]
                self.dlmatrix[item].right = self.dlmatrix[self.dlmatrix[item].number+1]
            elif item == self.items:
                self.dlmatrix[item].right = self.dlmatrix[0]
                self.dlmatrix[item].left = self.dlmatrix[self.dlmatrix[item].number-1]
                self.dlmatrix[item].below = self.dlmatrix[ref_lists[-1][1]]
                self.dlmatrix[item].above = self.dlmatrix[ref_lists[-1][-1]]
            else:
                self.dlmatrix[item].left = self.dlmatrix[self.dlmatrix[item].number-1]
                self.dlmatrix[item].right = self.dlmatrix[self.dlmatrix[item].number+1]
                self.dlmatrix[item].below = self.dlmatrix[ref_lists[item-1][1]]
                self.dlmatrix[item].above = self.dlmatrix[ref_lists[item-1][-1]]

        #link nodes
        for item in range(len(ref_lists)):
            for node in range(1, len(ref_lists[item])):
                if node == (len(ref_lists[item]) - 1):
                    self.dlmatrix[ref_lists[item][node]].below = self.dlmatrix[ref_lists[item][0]]
                    self.dlmatrix[ref_lists[item][node]].above = self.dlmatrix[ref_lists[item][node-1]]
                elif node == 0:
                    self.dlmatrix[ref_lists[item][node]].below = self.dlmatrix[ref_lists[item][node+1]]
                    self.dlmatrix[ref_lists[item][node]].above = self.dlmatrix[ref_lists[item][-1]]
                else:
                    self.dlmatrix[ref_lists[item][node]].below = self.dlmatrix[ref_lists[item][node+1]]
                    self.dlmatrix[ref_lists[item][node]].above = self.dlmatrix[ref_lists[item][node-1]]
        
        #link spacers
        for spacer in range(len(self.spacers_ref)):
            if spacer == 0:
                self.dlmatrix[self.spacers_ref[0]].below = self.dlmatrix[self.nodes_ref[spacer][-1]]
            elif spacer == (len(self.spacers_ref)-1):
                self.dlmatrix[self.spacers_ref[-1]].above = self.dlmatrix[self.nodes_ref[spacer-1][0]]
            else:
                self.dlmatrix[self.spacers_ref[spacer]].above = self.dlmatrix[self.nodes_ref[spacer-1][0]]
                self.dlmatrix[self.spacers_ref[spacer]].below = self.dlmatrix[self.nodes_ref[spacer][-1]]

    def create_dlmatrix(self):
        """Calls create_headers, create_nodes and create_links in correct order hence creating a dlmatrix"""
        self.create_headers()
        self.create_nodes()
        self.create_links()

    def output_solution(self, solution):
        """Formats solution outputted from AlgorithmX"""
        print(solution)

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

