
  "Comment": "Workflow to fetch data and store in S3",
  "StartAt": "FetchData",
  "States": {
    "FetchData": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:FetchDataLambda",
      "Next": "ConvertToParquet"
    },
    "ConvertToParquet": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:ConvertToParquetLambda",
      "Next": "StoreInS3"
    },
    "StoreInS3": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:StoreInS3Lambda",
      "End": true
    }
  }