from fileSorter import SortExtension
from orientation import orientationSort
from music import musicSort
from tvClean import tvClean

user_choice =  input('Choose what you want:\n\n(1) Sort files by extension \n(2) Sort videos by orientation \n(3) Remove site name from music title \n(4) Remove junk from movies & tv\n -> ')

raw_path = input('Provide the path to sort \n ->')

change_bracket = raw_path.replace('\\', '/')

path = change_bracket + '/'

if user_choice == '1':
    SortExtension(path)
elif user_choice == '2':
    orientationSort(path)
elif user_choice == '3':
    musicSort(path)
elif user_choice == '4':
    tvClean(path)

# OTHER IDEAS:
#sort tv shows by season



