import os

#Function for printing out array elements
def print_arr(arr):
    for item in arr:
        print(item)

#Search for a specified element in an array by keyword
def arr_find(arr, keyword):
    if keyword == None: return arr
    keyword = keyword.lower()
    search_result = []
    for item in arr:
        if item.lower().find(keyword) != -1: search_result.append(item)
    return search_result

#List every file of a given directory in an array
def read_dir(path, path_arr = []):
    path = path.replace("\\","/")
    for file in os.listdir(path):
        try:
            file_path = path+"/"+file
            path_arr.append(file_path)
            if os.path.isdir(file_path): read_dir(file_path, path_arr)
        except Exception as error:
            if type(error) == PermissionError:
                print(error)
            else:
                raise(error)
    return path_arr

#Initiation
if __name__ == "__main__":
    import sys
    import time

    args = [ os.getcwd(), None ]
    for i in range(len(sys.argv)-1):
        if i<len(args): args[i] = sys.argv[i+1]
        else: break;

    if not os.path.isdir(args[0]):
        args[1] = args[0];
        args[0] = os.getcwd();

    #Run cod
    timestamp = time.time()
    raw_data = read_dir(args[0].replace('\\', '/'))
    search = arr_find(raw_data, args[1])
    timestamp = time.time() - timestamp

    #Summary
    print_arr(search)
    print("\nReturned", len(search), "results\nTime elapsed:", timestamp)
