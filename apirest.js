const AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient();
 
exports.handler = async (event) => {
    const resourceId = event.pathParameters.resourceId;
    
    const params = {
        TableName: 'YourTableName',
        Key: {
            'PK': resourceId,  // Cambiar según tu diseño
            'SK': resourceId,  // Cambiar según tu diseño
        }
    };

    try {
        const data = await docClient.get(params).promise();
        return {
            statusCode: 200,
            body: JSON.stringify(data),
        };
    } catch (err) {
        return {
            statusCode: 500,
            body: JSON.stringify(err),
        };
    }
};
