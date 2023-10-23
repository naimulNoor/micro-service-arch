# Use the official Nginx image as the base image
FROM nginx:latest

# Remove the default Nginx welcome page
RUN rm /usr/share/nginx/html/index.html

# Copy your HTML files into the Nginx web root directory
COPY index.html /usr/share/nginx/html

# Expose port 80, which is the default port for HTTP
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]