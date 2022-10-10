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

def plot_runtime_search(max_length, iterations):
    #runtime = test_search(max_length, iterations)
    pass

def main():
    #try
    plot_runtime_construct(20, 40)
    plot_runtime_search()

if __name__ == '__main__':
    main()

