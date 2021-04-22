import os, sys, argparse, re  

def main(args):
    parseArgs(args)

def parseArgs(args):
    if args.folder:
        print(f"Starting to rename files in the single folder {args.folder}")
        renameFiles(args.folder)
    elif args.root_folder:
        print(f"Starting to rename files in sub folders to {args.root_folder}")
        renameFilesInFolders(args.root_folder)
    else:
        print("Change the code to match text for replacements and run with -r or -f parameter and the filepath to rename the files")
        print("For more info how to use this script use -h or --help")

def renameFiles(path, text=''): ### Function to rename files in a single folder
    local_count = 1
    for count, filename in enumerate(os.listdir(path)):
        old_path_name = os.path.join(path, filename)
        if os.path.isfile(old_path_name):
            replecement_regexp = '\s\d\d\s' ### Replace with the regexp that matches what you want to replace
            replacement_text = " {}E{:02d} ".format(text,local_count) ### Replace with the text you want to be replaced by replecement_regexp
            new_path_name = os.path.join(path, re.sub(replecement_regexp, replacement_text, filename))
            os.rename(old_path_name, new_path_name)
            local_count += 1

def renameFilesInFolders(path): ### Function to rename files in a multiple folders
    for count, filename in enumerate(os.listdir(path)):
        old_path_name = os.path.join(path, filename)
        text = "S{:02d}".format(count+1) ### Optinal text for filename from folder to folder
        if os.path.isdir(old_path_name):  
            renameFiles(old_path_name, text)
        elif os.path.isfile(old_path_name):  
            renameFiles(path, text) ### Remove or comment out this row if you dont want files in the root folder to change name and only the files in subfolders
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename files in folders. Change the code to match what your text replacements')
    parser.add_argument('-r', '--root_folder', help="Rename multiple files in multiple folders", metavar="Path_to_folder")
    parser.add_argument('-f', '--folder', help="Rename multiple files in singel folder", metavar="Path_to_folder")
    args = parser.parse_args()

    main(args)