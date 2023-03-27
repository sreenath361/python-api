# python-api


Step 1: clone the repo- https://github.com/sreenath361/python-api.git

Step 2: Run docker-compose up -d

It will spinup 4 docker container -> Fluentd -> ES -> Kibana -> App Container

# Kibana 
Kibana port: 5601

In the Kibana dashboard, create an index pattern(Fluentd) by following the instructions in the Kibana UI.
Once the index pattern is created, you can view logs in the Discover tab of the Kibana dashboard.
You can view the application logs in Kibana that are being forwarded successfully.
