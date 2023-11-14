from singleton_logger import SingletonLogger


def avg(*args):
    return sum(args)/len(args)

def flex(**kwargs):
    if "name" in kwargs:
        print(kwargs.get("name"))

    if "age" in kwargs:
        print(f"age: {kwargs.get('age')}")


if __name__ == "__main__":
    # l1 = SingletonLogger('app.log')
    # l2 = SingletonLogger('**ignored**')
    # assert l1 is l2
    #
    # l1.log('Writing to log 1')
    # l2.log('Writing to log 2')
    #
    # l1.close_log()
    # # l2.close_log()
    print(avg(1))
    print(avg(1, 2))
    print(avg(1, 2, 3))

    flex(name="Andrey", age="40", height="5'9""")