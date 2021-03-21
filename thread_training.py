import multiprocessing


def test_function():
    for i in range(19999999):
        pass


t1 = multiprocessing.Process(target=test_function())
t2 = multiprocessing.Process(target=test_function())
t1.start()
t2.start()
