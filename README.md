# Stock Market Data Pipeline
## Overview

Built an end-to-end serverless data engineering pipeline on AWS that ingests stock data, transforms it, stores it in a cloud data warehouse, and visualizes it in a BI dashboard.

## Architecture

<img width="644" height="561" alt="stockpipeline2 drawio" src="https://github.com/user-attachments/assets/8e7cf388-fda0-474a-9bc1-a8276c20f1ae" />

## Technologies Used

AWS S3

AWS Lambda

Amazon Redshift Serverless

Amazon QuickSight

IAM

VPC Networking

## Key Features

Event-driven ingestion

Secure IAM role configuration

Redshift COPY from S3

BI visualization with calculated metrics

## Challenges Solved

IAM role trust policies

Redshift Serverless default role errors

Region mismatch troubleshooting

Private VPC networking with QuickSight

Security group configuration

## Outcome

Successfully built a production-style analytics pipeline capable of loading, transforming, warehousing, and visualizing financial time-series data.
