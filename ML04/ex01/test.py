from YoungestFellah import youngest_fellah
from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15
print(youngest_fellah(data, 2004))
# Output
#{'f': 13.0, 'm': 14.0}
