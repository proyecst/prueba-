# prueba-# README de Proyecto Serverless en AWS

## Descripción del Proyecto

Este proyecto implementa una solución serverless en AWS utilizando una arquitectura basada en varios servicios de AWS que permiten la ingesta, transformación y consulta de datos. La aplicación se compone de los siguientes componentes clave:

- **AWS Step Functions**: Orquesta la ingesta y transformación de datos desde una API externa.
- **Amazon S3**: Almacena los datos transformados en formato Parquet y particionados.
- **Amazon Athena**: Permite realizar consultas SQL sobre los datos almacenados en S3.
- **AWS DynamoDB**: Almacena metadatos sobre los recursos definidos en la aplicación.
- **AWS Lambda**: Proporciona APIs REST para acceso a DynamoDB y S3.
- **API Gateway**: Expone los endpoints de las funciones Lambda.
- **AWS CloudFormation**: Automatiza la creación de los recursos necesarios.

## Requisitos Previos

Antes de comenzar, asegúrese de tener una cuenta de AWS y haber configurado los permisos necesarios para crear los recursos mencionados.

## Componentes del Proyecto

### AWS Step Functions

Se ha diseñado un flujo de trabajo en AWS Step Functions que realiza las siguientes tareas:

1. **Recuperar los datos desde una API externa** (como JSONPlaceholder).
2. **Transformar los datos** en formato Parquet o Avro.
3. **Particionar los datos** en S3 con la estructura: `datos/resource={resourceId}/datos.parquet`.

### Consultas a los Datos en S3

Para consultar los datos almacenados en S3 se ha configurado Amazon Athena, lo que permite ejecutar consultas SQL directamente sobre los archivos Parquet.

### DynamoDB

Se ha creado una tabla en DynamoDB para almacenar información sobre recursos definidos (ej. clientes, productos, pedidos), utilizando las mejores prácticas de modelado con:

- **Partition Key (PK)**
- **Sort Key (SK)**

Se implementan al menos tres patrones de acceso utilizando el método **Query**:

1. Obtener un recurso por su `resourceId`.
2. Obtener todos los datos relacionados con un identificador específico.
3. Consultar datos basado en un rango de fechas o una condición específica.

### API REST

Se han implementado dos APIs REST utilizando AWS Lambda:

- **Node.js**: Para recuperar datos de DynamoDB.
    - Endpoint: `GET /resource/{resourceId}`

- **Python**: Para recuperar datos de S3 en formato Parquet a través de Athena.
    - Endpoint: `GET /resource/{resourceId}`

### API Gateway

Se ha configurado el API Gateway para enrutar las solicitudes a las funciones Lambda y manejar las respuestas adecuadamente.

### CloudFormation

Se ha creado una plantilla de CloudFormation que automatiza la creación y configuración de los recursos necesarios, incluyendo:

- Tabla de DynamoDB
- Funciones Lambda para Node.js y Python
- API Gateway
- Flujo de trabajo en Step Functions
- Configuración de la tabla en Athena y la integración con S3

### Pruebas

Se han desarrollado scripts de prueba para validar que los endpoints funcionen correctamente y que la integración entre los componentes de la infraestructura funcione como se espera.

## Cómo Ejecutar el Proyecto

1. **Configurar AWS CLI**: Asegúrate de tener configurada la CLI de AWS con las credenciales adecuadas.
2. **Desplegar los Recursos**:
    - Utiliza la plantilla de CloudFormation para crear todos los recursos necesarios.
3. **Iniciar el Flujo de Trabajo**:
    - Ejecuta el flujo de trabajo en Step Functions para iniciar la ingesta y transformación de datos.
4. **Probar los Endpoints**:
    - Realiza solicitudes a los endpoints expuestos a través de API Gateway.

## Ejemplo de Uso

Un ejemplo de cómo realizar una consulta GET para recuperar datos de un recurso específico en DynamoDB:

```bash
curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/prod/resource/{resourceId}
```

## Mantenimiento

Para mantener el proyecto:

- Realiza pruebas periódicas de los endpoints.
- Monitorea el uso de recursos y ajusta la configuración según sea necesario.
  
## Contribución

Si deseas contribuir a este proyecto, siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
