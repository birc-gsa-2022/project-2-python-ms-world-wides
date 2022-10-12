import time
import matplotlib.pyplot as plt
import elv
import random

def generate_rand_seq(length_x):
    random.seed()
    a = ['a', 'c', 'g', 't']
    x = ""
    for i in range(length_x):
        x = "".join((x, random.choice(a)))
    return x

def test_construct_tree(max_length, iterations, string):
    runtime = {}
    for i in range(max_length):
        runtime_total = 0
        if (string == "wc"): 
            x = 'a'*max_length
        #run multiple times to get the average
        for j in range(iterations):
            if (string == "wc"): 
                x = x[:i]
            else: 
                x = generate_rand_seq(i) #back -> 
            # calc runtime
            startTime = time.time()
            elv.construct_tree(x)
            executionTime = (time.time() - startTime)
            runtime_total += executionTime
        runtime[i] = runtime_total/iterations # add time to value in sequence length key

    return(runtime)

def plot_runtime_construct(max_length, iterations):
    runtime = test_construct_tree(max_length, iterations, "")
    runtime_wc = test_construct_tree(max_length, iterations, "wc")
    plt.plot(runtime.keys(), runtime.values(), color="darkblue", label = f"with random sequence x")
    plt.plot(runtime_wc.keys(), runtime_wc.values(), color="red",label = f"with x = a^n" )
    plt.xlabel('Size of sequence x [bp]')
    plt.ylabel('Time [s]')
    plt.title(f'Runtime of the algorithm for constructing a suffixtree')
    plt.legend(loc="upper left")
    plt.show()

def plot_runtime_search(x_length, p_max_length, iterations):
    x = generate_rand_seq(x_length)
    T = elv.construct_tree(x)
    runtime = test_search(T, x, p_max_length, iterations)
    plt.plot(runtime.keys(), runtime.values(), color="darkblue")#, label = f"with random sequence x")
    #plt.plot(runtime_wc.keys(), runtime_wc.values(), color="red",label = f"with x = a^n" )
    plt.xlabel('Size of pattern p [bp]')
    plt.ylabel('Time [s]')
    plt.title(f'Runtime of the algorithm for searching a pattern in a suffixtree')
    #plt.legend(loc="upper left")
    plt.show()

def test_search(T, x, p_max_length, iterations):
    runtime = {}
    for i in range(5,p_max_length):
        runtime_total = 0
        #run multiple times to get the average
        for j in range(iterations):
            p = generate_rand_seq(i) 
            # calc runtime
            startTime = time.time()
            elv.match(p, x, T)
            executionTime = (time.time() - startTime)
            runtime_total += executionTime
        runtime[i] = runtime_total/iterations # add time to value in sequence length key
    return runtime
    
def main():
    #try
    #plot_runtime_construct(100, 2)
    plot_runtime_search(100,30,10)
if __name__ == '__main__':
    main()

