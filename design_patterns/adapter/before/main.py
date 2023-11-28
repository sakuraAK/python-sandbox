from mocks import VENDORS, CUSTOMERS
from customer import Customer
from vendor import Vendor
TYPE = 'customer'


def custom_print(**kwargs):
    if 'number' in kwargs:
        print(f"Name: {kwargs['name']}; Address:{kwargs['number']} {kwargs['street']}")
    else:
        print(f"Name: {kwargs['name']}; Address:{kwargs['address']}")
def main():
    if TYPE == 'customer':
        for customer in CUSTOMERS:
            custom_print(name=customer.name, address=customer.address)
    elif TYPE == 'vendor':
        for vendor in VENDORS:
            custom_print(name=vendor.name, number=vendor.number, street=vendor.street)
    else:
        raise ValueError(f"{TYPE} not supported")


if __name__ == "__main__":
    main()

