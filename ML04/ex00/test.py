from FileLoader import FileLoader


loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
# Output
#Loading dataset of dimensions 32561 x 15
loader.display(data, 12)
