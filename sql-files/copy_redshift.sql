COPY stock_prices
FROM 's3://My-Bucket-Name/processed/'
IAM_ROLE 'arn:aws:iam::142431531412:role/redshift-s3-role'
CSV
IGNOREHEADER 1;
