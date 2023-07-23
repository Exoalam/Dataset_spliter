import os
import shutil

def get_file_names_from_directory(directory_path):
    try:
        file_names = os.listdir(directory_path)
        return file_names
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def create_directory(directory_path):
    try:
        os.mkdir(directory_path)
        print(f"Directory created: {directory_path}")
    except FileExistsError:
        print(f"Directory already exists: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_file(source_file, destination_file):
    try:
        # Copy the file from source_file to destination_file
        shutil.copy(source_file, destination_file)
        print(f"File copied successfully from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"Source file not found: {source_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def find_substring_between_chars(input_string, start_char, end_char):
    start_index = input_string.find(start_char)
    end_index = input_string.find(end_char, start_index + 1) 

    if start_index != -1 and end_index != -1:
        substring = input_string[start_index + 1:end_index]
        return substring
    else:
        return None

directory_path = 'Screenshots'
output_path = 'Data/'

create_directory(output_path)
create_directory(output_path+'M')
create_directory(output_path+'F')
create_directory(output_path+'O')
for i in range(20,100,5):
    create_directory(output_path+f'{i}-{i+5}')



file_names = get_file_names_from_directory(directory_path)

for name in file_names:
    result = find_substring_between_chars(name,'_','Y')
    result = int(result)
    if result >= 20 and result <= 25:
        copy_file(directory_path+'/'+name,output_path+'20-25')
    elif result > 25 and result <= 30:
        copy_file(directory_path+'/'+name,output_path+'25-30')
    elif result > 30 and result <= 35:
        copy_file(directory_path+'/'+name,output_path+'30-35')
    elif result > 35 and result <= 40:
        copy_file(directory_path+'/'+name,output_path+'35-40')
    elif result > 40 and result <= 45:
        copy_file(directory_path+'/'+name,output_path+'40-45')
    elif result > 45 and result <= 50:
        copy_file(directory_path+'/'+name,output_path+'45-50')
    elif result > 50 and result <= 55:
        copy_file(directory_path+'/'+name,output_path+'50-55')
    elif result > 55 and result <= 60:
        copy_file(directory_path+'/'+name,output_path+'55-60')
    elif result > 60 and result <= 65:
        copy_file(directory_path+'/'+name,output_path+'60-65')
    elif result > 65 and result <= 70:
        copy_file(directory_path+'/'+name,output_path+'65-70')
    elif result > 70 and result <= 75:
        copy_file(directory_path+'/'+name,output_path+'70-75')
    elif result > 75 and result <= 80:
        copy_file(directory_path+'/'+name,output_path+'75-80')
    elif result > 80 and result <= 85:
        copy_file(directory_path+'/'+name,output_path+'80-85')
    elif result > 85 and result <= 90:
        copy_file(directory_path+'/'+name,output_path+'85-90')
    elif result > 90 and result <= 95:
        copy_file(directory_path+'/'+name,output_path+'90-95')
    elif result >= 95 and result <= 100:
        copy_file(directory_path+'/'+name,output_path+'95-100')

    result2 = find_substring_between_chars(name,',','_')
    if result2 == 'M':
        copy_file(directory_path+'/'+name,output_path+'M')
    elif result2 == 'F':
        copy_file(directory_path+'/'+name,output_path+'F')
    elif result2 == 'O':
        copy_file(directory_path+'/'+name,output_path+'O')
