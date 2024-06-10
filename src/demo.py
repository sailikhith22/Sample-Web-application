from extractinginfo import  get_answers
from utils import get_columns, get_dataframe
message = {'name': 'sdfasdf', 'age': 13123, 'gender': 'male'}

df = get_dataframe(message)
print(df)
print("shape is",df.shape)
