#!/usr/bin/env python3
""" Solution: Multiply two matrices """

import random
import time
import math
import multiprocessing as mp

""" sequential implementation of matrix multiplication """
def seq_matrix_multiply(A, B):
    # establish a few useful variables
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])
    if num_cols_A != num_rows_B:
        raise ArithmeticError('Invalid dimensions; Cannot multiply {}x{}*{}x{}'.format(num_rows_A, num_cols_A, num_rows_B, num_cols_B))
    # compute a return matrix product C = A*B
    C = [[0] * num_cols_B for i in range(num_rows_A)]
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            for k in range(num_cols_A): # same as num_rows_B
                C[i][j] += A[i][k] * B[k][j]
    return C

""" parallel implementation of matrix multiplication """

def helper(a_rowid,b_columnid,b_rowcount,A,B):
    #print("called with",a_rowid,b_columnid,b_rowcount)
    result=0
    #k=0
    #print(A[a_rowid])
    for k,rowdata in enumerate(A[a_rowid]):
        #print(rowdata,B[k][b_columnid])
        result+=rowdata*B[k][b_columnid]
        #print(result)
        k+=1
    #print(result)
    #time.sleep(5)
    return {(a_rowid,b_columnid):result}
        



def par_matrix_multiply(A, B):
    # establish a few useful variables
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])
    if num_cols_A != num_rows_B:
        raise ArithmeticError('Invalid dimensions; Cannot multiply {}x{}*{}x{}'.format(num_rows_A, num_cols_A, num_rows_B, num_cols_B))
    C = [[0] * num_cols_B for i in range(num_rows_A)]
    pool=mp.Pool(mp.cpu_count())
    result_operations=[]
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            result_operations.append((i,j,num_rows_B,A,B))
    result=pool.starmap(helper,result_operations)
    for data in result:
        #print(data)
        i,j=list(*data.keys())
        value=int(list(data.values())[0])
        C[i][j]=value
    pool.close()
    return C

if __name__ == '__main__':
    NUM_EVAL_RUNS = 1
    A = [[random.randint(10,100) for i in range(500)] for j in range(500)]
    B = [[random.randint(10,100) for i in range(500)] for j in range(500)]

    print('Evaluating Sequential Implementation...')
    sequential_result = seq_matrix_multiply(A, B) # "warm up"
    sequential_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_matrix_multiply(A, B)
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print('Evaluating Parallel Implementation...')
    parallel_result = par_matrix_multiply(A, B)  # "warm up"
    parallel_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_matrix_multiply(A, B)
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    #print(sequential_result)
    #print(parallel_result)
    if sequential_result != parallel_result:
        raise Exception('sequential_result and parallel_result do not match.')
    print('Average Sequential Time: {:.2f} ms'.format(sequential_time*1000))
    print('Average Parallel Time: {:.2f} ms'.format(parallel_time*1000))
    print('Speedup: {:.2f}'.format(sequential_time/parallel_time))
    print('Efficiency: {:.2f}%'.format(100*(sequential_time/parallel_time)/mp.cpu_count()))
