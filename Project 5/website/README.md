
Step 1:

    I went to a web browser and typed this url in: 

        https://www.docker.com/products/docker-desktop
    
    I then clicked on the button with the text "Download Docker Desktop Windows"

Step 2:
    // to build the container from the DockerFile

            FROM nginx
            
            COPY index.html /usr/share/nginx/html

            CMD ["/usr/share/nginx/html/index.html"]
        
    //Then include the following command to include an image using a Dockerfile:

                docker build -t d5:latest -t d5:0.2 .

   

Step 3:

    //to run the container:
    docker run --name d5.2 -d -p 8080:80 d5

Step 4:

    //type down the following to create the container:

        docker run -d -p 8080:80 d5
    
    //then do the following to view the project running in the container

        go to the browser and type "localhost:8080"
        or I could type down my IP adress with the 8080 such as "192.168.1.101:8080"
