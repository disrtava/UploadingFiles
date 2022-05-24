import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,access_token,file_to,file_from):
        dbx = dropbox.Dropbox(access_token)
        for root , dirs , files in os.walk(file_from):
            for name in files:
                name1 = os.path.join(root,name)
            for name in dirs:
                path = os.path.join(root,name)
        with open(path, 'rb') as a:
            dbx.files_upload(a.read(),path,mode=WriteMode('overwrite')) 

def main():
    access_token = 'sl.BH3jyEJaAwTLjDzi6LU_zV6y1r4nslhqZgds5MkG6KpelzSfQ8rcBr4WGuNxP1GUzH6Tyc5wq6QSideAw_8xQup743GKvr4itxqEJblvGiK06ii5r8ecQ7cEXU3K32jV349CmPE'
    transferData = TransferData(access_token)
    
    file_from = input("Enter the folder you want to be uploaded")
    file_to = input("Enter the full path to the folder you want to be uploaded")
    TransferData.upload_file(file_from,file_to)

if __name__ == '__main__' :
    main()