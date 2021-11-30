import multiprocessing
import time

def count(name):
   for i in range(1,50001):
     print(name, " : ", i)

if __name__ == '__main__':

  start_time = time.time()



  num_list = ['p1', 'p2', 'p3', 'p4']

  pool = multiprocessing.Pool(processes=2)
  pool.map(count, num_list)
  pool.close()
  pool.join()

  print("=====%s seconds ===" % (time.time() - start_time))