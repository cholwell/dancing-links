import exact_cover
import sudoku 

class AlgorithmDLX():
    """
    Implements algorithmX using the dancing links method
    
    Attributes:
        - problem, -, problem to be solved
        - problem_type, str, specifies problem type to be solved
        - solution_counter, int, counts how many solutions have been found
        - solutions, list, contains the solutions that have been found
        - head, Header object, Header zero of problem attribute
        - algorithm_on, bool, flag variable used to start and stop algorithm
        - display_options, bool, algorithm shows current choice of options if set to true
        - i, Header, internal algorithm variable, at each level l initially set to item to be covered
        - l, int, current level algorithm is on
        - x_l, list, contains reference number of Node chosen at level l 
        - x_l_display, list, printed if display_options is True

    Methods:
        - record_solution(), records solution to solutions attribute when one is found
        - mrv_header(), implements mrv heuristic for selecting header
        - init_sudoku(), prepares for algorithmX given partial sudoku 
        - cover(), cover operation
        - hide(), hide operation
        - uncover(), uncover operation
        - unhide(), unhide operation
        - algorithm_x(), when called starts algorithm by performing steps X1, X2
        - X3(), step X3 of algorithmX
        - ...
        - X8(), step 8 of algorithmX
    """

    def __init__(self, dlmatrix, problem_type, display_options = False):
        self.problem = dlmatrix
        self.problem_type = str(problem_type)
        self.solution_counter = 0
        self.solutions = []
        self.head = self.problem.dlmatrix[0]
        self.algorithm_on = True
        self.display_options = display_options
        #attributes used internally in algorithm
        self.i = None
        self.l = 0
        self.x_l = []
        self.x_l_display = []
        #run algorithm when instance of class is created
        self.algorithm_dlx()


    def record_solution(self):
        """Records found solution to solutions list when a solution is found"""
        self.solutions.append([])
        for x in range(len(self.x_l)):
            self.solutions[self.solution_counter].append(self.x_l[x].option)

    def mrv_header(self):
        """Iterates right through currently linked headers and finds the one with the smallest len value,
        if multiple selects the first found"""
        min_header = self.head.right
        test_next = self.head.right
        while test_next != self.head:
            if test_next.len < min_header.len:
                min_header = test_next
                test_next = test_next.right
            else:
                test_next = test_next.right
        return min_header

    def init_sudoku(self):
        """Covers appropriate items based off partial sudoku solution in preparation for algorithmX"""
        for item in (self.problem.partial_solution):
            self.cover(self.problem.dlmatrix[item])
    
    def cover(self, i):
        """Cover operation"""
        p = i.below
        while p != i:
            self.hide(p)
            p = p.below
        i.unlink_hor()

    def hide(self, p):
        """Hide operation"""
        q = self.problem.dlmatrix[p.number+1]
        while q != p:
            x = q.top 
            if x <= 0:
                q = q.above
            else:
                q.unlink_vert()
                self.problem.dlmatrix[x].len -= 1
                q = self.problem.dlmatrix[q.number+1]


    def uncover(self, i):
        """Uncover operation"""
        i.link_hor()
        p = i.above
        while p != i:
            self.unhide(p)
            p = p.above

    def unhide(self, p):
        """Unhide operation"""
        q = self.problem.dlmatrix[p.number-1]
        while q != p:
            x = q.top
            if x <= 0:
                q = q.below
            else:
                q.link_vert()
                self.problem.dlmatrix[x].len += 1
                q = self.problem.dlmatrix[q.number-1]

    def algorithm_dlx(self):
        """Implements algorithmX"""
        #X1
        if self.problem_type == 'sudoku':
            self.init_sudoku()

        #X2
        while self.algorithm_on == True:
            if self.head.right == self.head:
                print('solution found')
                self.record_solution()
                self.solution_counter += 1
                self.X8()
            else:
                self.X3()

    def X3(self):
        """X3"""
        self.i = self.mrv_header()
        self.X4()

    def X4(self):
        """X4"""
        self.cover(self.i)
        self.x_l.append(self.i.below)
        if self.display_options == True:
            if self.i.below.number > len(self.problem.headers_ref):
                self.x_l_display.append(self.i.below.option)
            else:
                self.x_l_display.append('backtrack')
            print(self.x_l_display)
        self.X5()

    def X5(self):
        """X5"""
        if self.x_l[self.l] == self.i:
            self.X7()
        else:
            p = self.problem.dlmatrix[self.x_l[self.l].number + 1]
            while p != self.x_l[self.l]:
                j = p.top 
                if j <= 0:
                    p = p.above
                else:
                    self.cover(self.problem.dlmatrix[j])
                    p = self.problem.dlmatrix[p.number + 1]
            self.l += 1

    def X6(self):
        """X6"""
        p = self.problem.dlmatrix[self.x_l[self.l].number - 1]
        while p != self.x_l[self.l]:
            j = p.top
            if j <= 0:
                p = p.below
            else:
                self.uncover(self.problem.dlmatrix[j])
                p = self.problem.dlmatrix[p.number - 1]
        self.i = self.problem.dlmatrix[self.x_l[self.l].top]
        self.x_l[self.l] = self.x_l[self.l].below
        self.X5()

    def X7(self):
        """X7"""
        self.uncover(self.i)
        self.x_l.pop()        
        if self.display_options == True:
            self.x_l_display.pop()
        self.X8()

    def X8(self):
        """X8"""
        if self.l == 0:
            self.algorithm_on = False
            if len(self.solutions) == 0:
                print('\nno solutions')
            else:
                print('\nall solutions found')
                if self.solution_counter == 1:
                    print('there is 1 solution\n')
                    self.problem.output_solution(self.solutions[0])
                else:
                    print('there are ' + str(self.solution_counter) + ' solutions\n')
                    for solution in range(len(self.solutions)):
                        self.problem.output_solution(self.solutions[solution])
        else:   
            self.l -= 1
            self.X6()                      