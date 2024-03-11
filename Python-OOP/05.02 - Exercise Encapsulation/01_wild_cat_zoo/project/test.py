from project.zoo import Zoo
from project.vet import Vet
z = Zoo("Some Zoo", 1500, 1, 1)
print(z.hire_worker(Vet("I am Vet", 20, 500)))
# self.assertEqual(res, "I am Vet the Vet hired successfully")
print(len(z.workers))
print(z._Zoo__workers_capacity)#, 1)
x = 5