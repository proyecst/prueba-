Resources:
  YourDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: YourTableName
      AttributeDefinitions:
        - AttributeName: PK
          AttributeType: S
        - AttributeName: SK
          AttributeType: S
      KeySchema:
        - AttributeName: PK
          KeyType: HASH
        - AttributeName: SK
          KeyType: RANGE
      BillingMode: PAY_PER_REQUEST

  FetchDataLambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Handler: fetch_data.lambda_handler
      Role: !GetAtt LambdaExecutionRole.Arn
      Code:
        ZipFile: |
          (Tu código aquí)
      Runtime: python3.8

  ApiGateway:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Name: "API"
