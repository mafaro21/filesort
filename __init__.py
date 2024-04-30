from fileSorter import SortExtension
from  orientation import orientationSort

user_choice =  input('Choose what you want:\n\n(1) Sort files by extension \n(2) Sort files by orientation \n -> ')

raw_path = input('Provide the path to sort \n ->')

change_bracket = raw_path.replace('\\', '/')

path = change_bracket + '/'

if user_choice == '1':
    SortExtension(path)
elif user_choice == '2':
    orientationSort(path)

# OTHER IDEAS:
# VIDEO ORIENTATION



