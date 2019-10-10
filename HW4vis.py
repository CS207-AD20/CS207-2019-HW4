from ADvis.ADnum import ADnum
import ADvis.ADgraph as ADgraph
import ADvis.ADmath as ADmath

print('This script runs the same series of commands as the GUI but without the GUI interface to allow you to visualize functions.')

def get_x():
    xval = input('At what value of x would you like to evaluate the function and its derivative?\n')
    try:
        x = ADnum(float(xval), ins=2, ind=0)
    except:
        print('x value must be a float.')
        x = get_x()
    return x

def get_y():
    yval = input('At what value of y would you like to evaluate the function and its derivative?\n')
    try:
        y = ADnum(float(yval), ins=2, ind=1)
    except:
        print('y value must be a float.')
        y=get_y()
    return y

def get_f():
    fin = input('Enter the function of x and y that you wish to visualize.  Use x and y to represent the inputs.  (Note: This script will not accept any special functions (trigonometric, exponential, etc.), but for HW4 you should not need any of these.)\n')
    try:
        func = lambda x,y: eval(fin)
        func(1, 1)
    except:
        print('Syntax error in your expression.  Please try again.')
        func = get_f()
    return func

print('AUTOMATIC DIFFERENTIATION VISUALIZATION\n')


x = get_x()
y = get_y()
func = get_f()

f = func(x, y)

print('The value of your function at ({},{}) is {}'.format(x.val, y.val, f.val))
print('The derivative of your function at ({},{}) is {}'.format(x.val, y.val, f.der))


print('\n\nFORWARD MODE AUTOMATIC DIFFERENTIATION\n')

print('The computational table for forward mode of your function is:')
table = ADgraph.gen_table(f)
print(table)

G, edge_labs, pos, labs = ADgraph.get_graph_setup(f)

input('\nWe can visualize the corresponding forward mode graph of your function. (Hint: Maximizing the graph window may make the graph easier to read.) When you are done looking at the graph, close the plot window to proceed to reverse mode.  Hit Enter to continue.')

ADgraph.draw_graph2(f, G, edge_labs, pos, labs)

print('\n\n\nREVERSE MODE AUTOMATIC DIFFERENTIATION\n')

input('Now let\'s think about reverse mode.  We will first visualize the entire reverse graph.  (This is the graph you should save for HW4.)  When you are done, close the plot window to proceed.  Hit Enter to continue.')
ADgraph.draw_graph_rev2(f, G, edge_labs, pos, labs)

input('\nLet\'s step through the graph traversal for using reverse mode to find the partial derivative with respect to x.  When the plot window launches, click on it, and follow the instructions to step through the calculation (using the arrowkeys on the keyboard).  When you are done, close the plot window.  Hit Enter to continue.')
ADgraph.draw_graph_rev_dynamic(f, x.revder(f)[1], G, edge_labs, pos, labs, x.revder(f)[0])


input('\nLet\'s step through the graph traversal for using reverse mode to find the partial derivative with respect to y.  When the plot window launches, click on it, and follow the instructions to step through the calculation (using the arrowkeys on the keyboard).  When you are done, close the plot window.  Hit Enter to continue.')
ADgraph.draw_graph_rev_dynamic(f, y.revder(f)[1], G, edge_labs, pos, labs, y.revder(f)[0])

print('\nYou have completed the visualization of this function.  Run the script again if you want to try a different function.')
