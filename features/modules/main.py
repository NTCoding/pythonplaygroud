import sys

from dataaccess import DataAccess
from servicelayer import ApplicationService

db = DataAccess()
service = ApplicationService(db)
data = service.findAllCustomersForBusiness(123)

print(data)

