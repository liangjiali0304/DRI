import pysftp
import os
global filepath
filepath = []

def get_dir():
    dirs=[]
    try:
        directory_structure = sftp.listdir()
        for attr in directory_structure:
            dirs.append(attr)
    except:
        dirs=[]
    return dirs

def goDir(name):
    sftp.chdir(name)

def goDeep():
    global filepath
    first = get_dir()
    # recursion base case
    if len(first) == 0:
        # Go back one dir
        goDir("..")
        return

    for i in first:
        print(i)
        print(sftp.getcwd())
        if len(i) > 1:
            print("====================\
                =======================\
                ==========================")
            filepath.append(str(sftp.getcwd())+'/'+str(i))
        else:
            goDir(i)
            goDeep()
    return goDir("..")
        

with pysftp.Connection('45.33.47.227', username='jarjar', \
    password='mesaj@rj@r') as sftp:
        first_level = ['K','S','U']
        #print(os.getcwd())
        #sftp.put('/my/local/filename')  # upload file to public/ on remote
        #sftp.get('README_first.txt','./TUTORIAL.txt')         # get a remote file
        #for i in first_level:
        #    goDir(i)
        
        
        goDir('S')
        goDeep()

        for file in filepath:
            print(file)
            sftp.get(file) 
        '''
        #sftp.chdir('/H')
        first = get_dir()
        print(first)
        goDir(first[0])
        first = get_dir()
        print(first)
        print(sftp.getcwd())
        sftp.chdir('..')
        print(sftp.getcwd())
        #goDir(first[0])
        #first = get_dir()
        #print(first)
        #goDir('K')
        #print_dir()
        #sftp.chdir('/Y')
        #goDir('/Y')
        #print(sftp.getcwd())
        #listdir
        '''
