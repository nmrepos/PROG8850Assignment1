FROM mcr.microsoft.com/devcontainers/universal:latest

# Install MySQL
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server && \
    apt-get clean

# Copy custom init script into container
COPY init-mysql.sh /usr/local/bin/init-mysql.sh
RUN chmod +x /usr/local/bin/init-mysql.sh

# Ensure MySQL runs and setup is done during container build
RUN /usr/local/bin/init-mysql.sh
