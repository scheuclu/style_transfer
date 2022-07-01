from google.cloud import storage
from torchvision.utils import save_image
import os

storage_client = storage.Client()


def write_image(tensor, folder, filename):
    bucket = storage_client.get_bucket('f1-betting-313907.appspot.com')
    blob = bucket.blob(f'style_transfer/{folder}/{filename}.jpg')
    save_image(tensor, f"{filename}.jpg")
    blob.upload_from_filename(f"{filename}.jpg")
    os.remove(f"{filename}.jpg")
    print(f"Wrote {folder}/{filename}.jpg")


# Get all the final images
if __name__ == "__main__":
    bucket = storage_client.get_bucket('f1-betting-313907.appspot.com')

    blobs = list(bucket.list_blobs())
    for blob in blobs:
        if blob.name.startswith('style_transfer') and "final" in blob.name:
            filename = blob.name.split('/')[1]+"_final.jpg"
            filename = f"/Users/lukas/Desktop/style_transfer_results/{filename}"
            print(filename)
            blob.download_to_filename(filename)