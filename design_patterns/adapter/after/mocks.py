import sys
sys.path.append('C:\\Users\\andre\\dev\\python-sandbox\\design_patterns\\adapter')

from before import Customer
from before import Vendor
from before import Supplier
from customer_adapter import CustomerAdapter
from vendor_adapter import VendorAdapter
from supplier_adapter import SupplierAdapter



CUSTOMERS = [CustomerAdapter(Customer('IGA', 'Saint Catherine 11')), CustomerAdapter(Customer('Metro', 'Van Horne 25'))]
VENDORS = [VendorAdapter(Vendor('Wholefood', 235, 'Sesame street')), VendorAdapter(Vendor('Kirkland', 404, 'King'))]
SUPPLIERS = [SupplierAdapter(Supplier('John', 'Doe', 'Saint Catherine 11')), SupplierAdapter(Supplier('Jane', 'Doe', 'Van Horne 25'))]