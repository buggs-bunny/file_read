'''file1= open('file_1.txt','r')
f=file1.read()

print(f)
file1.close()'''
def display_file_content(filename):
    try:
        with open(filename,'r') as f:
            for line in f:
                print(line.rstrip())
    except FileNotFoundError:
            print("File not found")
    except Exception as e:
            print("Something went wrong")

if __name__ == '__main__':
    display_file_content("file_1.txt")