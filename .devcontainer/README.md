# Notes
* Docker builds images based on the context directory (the same directory the Dockerfile is located in).  If you need to copy files or directories into the Docker container, they must be located in the same directory where the Dockerfile is placed.
  
> COPY <local_path> <container_path>