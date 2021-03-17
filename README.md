# mapproxy-config-download

Use to download file from object storage.

Usage:

1. `git clone <repository>`
2. run  `pip3 install -r ./requirements.txt`
3. configure custom env values in 's3downloader.py' or declare your machine envs (as below)
4. run `python3 s3downloader.py`

Run As Docker:
1. run `docker build` to build an image
2. run with volume to the declared output destination `docker run -v /external/path:declared/output/path <image name/id>`
   or specify env  with "-e" flag: `docker run -v /external/path:declared/output/path -e S3_BUCKET='my-bucket' <image name/id>`

Configurations:

`FILE_PROVIDER` - **REQUIRED**, can be: 's3' or 'fs'

if `FILE_PROVIDER` set for 's3':

`OUTPUT_DESTINATION` - default to 'downloads' - change to the directory name you want to save the file to (create if not exists) 

`S3_ENDPOINT_URL` - default to 'http//localhost:9000'

`AWS_ACCESS_KEY_ID` - default to 'minioadmin'

`AWS_SECRET_ACCESS_KEY` - default to 'minioadmin'

`S3_BUCKET` - default to 'mybucket'

`AWS_HTTPS` - default to False

`S3_OBJECT_KEY` - default to 'mapproxy.yaml'

if `FILE_RPOVIDER` set for 'fs':

`OUTPUT_DESTINATION` - default to 'downloads' - change to the directory name you want to save the file to (create if not exists) 

`SOURCE_FILE` - if `FILE_PROVIDER` is set to 'fs, set the path to the source file you want to copy 