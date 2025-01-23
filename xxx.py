import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    service_name ="s3",
    endpoint_url = f"{os.getenv('CLOUDFLARE_R2_ENDPOINT_URL')}",
    aws_access_key_id = f"{os.getenv('CLOUDFLARE_R2_ACCESS_KEY')}",
    aws_secret_access_key = f"{os.getenv('CLOUDFLARE_R2_SECRET_KEY')}",
    region_name=f"{os.getenv('CLOUDFLARE_R2_REGION')}", # Must be one of: wnam, enam, weur, eeur, apac, auto
)


# Get object information
object_information = s3.head_object(
                        Bucket=f"{os.getenv('CLOUDFLARE_R2_BUCKET_NAME')}",
                        Key="short-button.jpg")
print(object_information)

# # Upload/Update single file
# s3.upload_fileobj(io.BytesIO(file_content), <R2_BUCKET_NAME>, <FILE_KEY_NAME>)

# # Delete object
# delete = s3.delete_object(Bucket=f"{os.getenv('CLOUDFLARE_R2_BUCKET_NAME')}",
#                          Key="short-button.jpg")

# print(delete)