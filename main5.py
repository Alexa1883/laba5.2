class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(selfs, new_kg):
        if isinstance(new_kg, (int, float)):
            selfs.__kg = new_kg
        else:
            raise ValueError("Килограммы должны быть числом")

weight = KgToPounds(10)

print(f"{weight.kg} кг = {weight.to_pounds():.2f} фунтов")

try:
    weight.kg = "пять"
except ValueError as e:
    print(e)
