import pandas as pd
from tabulate import tabulate

import s3fs
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import Table
import os

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token=os.environ["AWS_SESSION_TOKEN"]

s3_uri = "s3://msd-s3-delta-dev-use-01/catalog/2c14f558-aacf-57fd-9f9f-8aef29940248/3372946ca3/seasonality/seasonality-bug-event-freq/post_process_out/"

fs = s3fs.S3FileSystem(
    anon=False,
    use_ssl=True,
    client_kwargs={
        "region_name": "us-east-1",
        "aws_access_key_id": aws_access_key_id,
        "aws_secret_access_key": aws_secret_access_key,
        "verify": True,
        "aws_session_token":aws_session_token
    }
)
print(fs)

s3_filepaths = [path for path in fs.ls(s3_uri)
                if path.endswith('.parquet')]
pf = pq.ParquetDataset(
    s3_filepaths,
    filesystem=fs)
df = pf.read().to_pandas()
print(pf.schema)
print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid'))