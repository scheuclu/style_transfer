# Imports the Google Cloud client library
from google.cloud import storage
from torchvision.utils import save_image
# Instantiates a client
storage_client = storage.Client()

import os



def write_image(tensor, folder, filename):
    bucket = storage_client.get_bucket('f1-betting-313907.appspot.com')
    blob = bucket.blob(f'style_transfer/{folder}/{filename}.jpg')
    save_image(tensor, f"{filename}.jpg")
    blob.upload_from_filename(f"{filename}.jpg")
    os.remove(f"{filename}.jpg")
    # with blob.open('wb') as f:
    #     save_image(tensor, f.)


