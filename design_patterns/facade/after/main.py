from get_users import PROVIDER
from get_users.facade_factory import FacadeFactory

if __name__ == "__main__":
    facade = FacadeFactory.create_facade(PROVIDER)
    facade.get_users()

