COPY stock_prices
FROM 's3://stock-pipeline-bucket1/processed/'
IAM_ROLE 'arn:aws:iam::343218202970:role/redshift-s3-role'
CSV
IGNOREHEADER 1;
