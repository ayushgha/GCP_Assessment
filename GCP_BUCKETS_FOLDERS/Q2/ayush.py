from google.cloud import storage
import os

BUCKET_NAME = 'ayush-bucket1'
DOWNLOAD_FOLDER = 'Folder1'
DESTINATION_FOLDER = 'Ans/'

# make destination folder in local machine
try:
    os.mkdir(DESTINATION_FOLDER)
except Exception as e:
    print('Destination folder already exists.')

def main():
    client = storage.Client()

    bucket = client.get_bucket(BUCKET_NAME)

    blobs = bucket.list_blobs()

    for blob in blobs:
        
        folders = DESTINATION_FOLDER + ''
        
        if blob.name.startswith(DOWNLOAD_FOLDER) and blob.name[-1] != '/':
            
            folder_struct = blob.name.split('/')
            
            for folder in folder_struct[:-1]:
                folders += folder + '/'
                try:
                    os.mkdir(fold)
                except Exception as e:
                    pass
            
            b.download_to_filename(folders + folder_struct[-1])

    print('Bucket structure has been re created in the local shell')

if __name__ == '__main__':
    main()
