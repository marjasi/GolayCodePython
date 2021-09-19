class Vector:
    """Vektoriaus klase. Vektorius yra elementu kolekcija - vienmatis masyvas."""

    # Vektoriaus elementu masyvas.
    values = []

    def __init__(self, vectorLength):
        """Sukuriamas nurodyto ilgio vektorius."""
        self.values = [vectorLength]
