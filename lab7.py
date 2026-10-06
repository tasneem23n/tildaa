class DictHash:
    def __init__(self):
        # Skapar en tom dictionary som hashtabell
        self.table = {}

    def store(self, nyckel, data):
        """Lagrar data med nyckel som key."""
        self.table[nyckel] = data

    def search(self, nyckel):
        """Slår upp nyckel och returnerar värdet, eller None om det inte finns."""
        return self.table.get(nyckel, None)

    # Extra metod: gör att man kan skriva d[nyckel]
    def __getitem__(self, nyckel):
        return self.search(nyckel)

    # Extra metod: gör att man kan skriva if nyckel in d
    def __contains__(self, nyckel):
        return nyckel in self.table

