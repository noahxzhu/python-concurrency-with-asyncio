from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    shared_int.get_lock().acquire()
    shared_int.value = shared_int.value + 1
    shared_int.get_lock().release()


if __name__ == "__main__":
    for _ in range(100):
        integer = Value("i", 0)
        proces = [
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
        ]

        [p.start() for p in proces]
        [p.join() for p in proces]
        print(integer.value)
        assert integer.value == 2
