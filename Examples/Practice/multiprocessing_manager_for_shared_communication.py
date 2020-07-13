from multiprocessing import Process, Manager


def test1(d, l):
    d['test1'] = "Hello"
    l.append('test1')
    print("test1 done")


def test2(d, l):
    d['test2'] = "Hello"
    l.append('test2')
    print("test2 done")


initial_list_value = [10, 20]
m = Manager()
d = m.dict()
l = m.list(initial_list_value)

d['initial'] = "something"

p1 = Process(target=test1, args=(d, l))
p2 = Process(target=test2, args=(d, l))
p1.start()
p2.start()

p1.join()
p2.join()

print("Dict" + str(d))
print("List" + str(l))
