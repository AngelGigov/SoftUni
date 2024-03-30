from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):

    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)


    def drive(self, mileage: float):
        # Calculate the percentage of max mileage passed
        mileage_percentage = (mileage / self.max_mileage) * 100

        # Round the percentage to the closest integer
        mileage_percentage = round(mileage_percentage)

        # Reduce the battery level by the calculated percentage
        self.battery_level -= mileage_percentage
        if self.battery_level < 0:
            self.battery_level = 0
