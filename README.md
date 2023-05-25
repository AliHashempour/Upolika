# Upolika
A simple micro service banking system management developed with [Flask](https://github.com/pallets/flask), using [RabbitMQ](https://github.com/rabbitmq), [mongodb](https://github.com/mongodb/mongo), [redis](https://github.com/redis/redis) and [docker](https://github.com/docker).  
## features
Authentication: users can create account and login to the application, based on token authentication.  

Transaction: users can add have transactions for their accounts and they can deposit or withdrawal.  

Admin: administrator role can have the list of all users with their accounts and transactions.The admin can add or remove users or see all of their information including their accounts and transactions logs.  

## how to run  
You can build the docker image by 
`docker build -t upolika:v1 .` and run the docker image.  
The other way is running the `start.sh`. 