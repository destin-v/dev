# Notes

## Dockerfile
* The dockerfile will be the primary method for building and maintaining images.
* Dockerfiles encapsulate all of the OS, environmental variables, and configurations need to run your programs.
## Context Directory
* By default Dockerfiles are only aware of what is in their **context directory**.  A context directory is the directory where a Dockerfile is located in.  It cannot access any files outside of the context directory.
* The context directory can be set from the command line or from a <code>docker_compose.yml</code> file.
## Docker Compose
* Allows you to create multiple different builds using different Dockerfiles.
* You can also set a new context directory from the <code>docker_compose.yml</code> file.
## Copying Directories / Files
* Docker builds images based on the context directory (the same directory the Dockerfile is located in).  This is the 

* If you need to copy files or directories into the Docker container, first put them in an **artifact** directory that can be seen from the context.
  
> COPY <artifact_directory> <container_path>