import pandas as pd
poids = pd.Series([3, 7, 12])
animal = pd.Series(["chat", "chien", "koala"])
animaux = pd.DataFrame(zip(animal, poids), columns=["animal", "poids"])
