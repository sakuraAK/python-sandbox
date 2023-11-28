from mocks import VENDORS, CUSTOMERS, SUPPLIERS
TYPE = 'supplier'


def custom_print(**kwargs):
    if 'number' in kwargs:
        print(f"Name: {kwargs['name']}; Address:{kwargs['number']} {kwargs['street']}")
    else:
        print(f"Name: {kwargs['name']}; Address:{kwargs['address']}")
def main():
    data = []
    if TYPE == 'customer':
        data = CUSTOMERS
    elif TYPE == 'vendor':
        data = VENDORS
    elif TYPE == 'supplier':
        data = SUPPLIERS
    else:
        raise ValueError(f"{TYPE} not supported")

    for obj in data:
        custom_print(name=obj.name(), address=obj.address())

if __name__ == "__main__":
    main()

