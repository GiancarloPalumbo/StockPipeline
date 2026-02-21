# Stock Market Data Pipeline
## Overview

Built an end-to-end serverless data engineering pipeline on AWS that ingests stock data, transforms it, stores it in a cloud data warehouse, and visualizes it in a BI dashboard.

## Architecture

(Insert architecture.png)

## Technologies Used

AWS S3

AWS Lambda

Amazon Redshift Serverless

Amazon QuickSight

IAM

VPC Networking

## Key Features

Event-driven ingestion

Automated transformation

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
