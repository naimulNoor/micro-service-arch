Project Report: Micro Service Arch

Services :
Image-to-text, Text-to-Speech, and Text Translation API Integration

Project Overview 

Project Title: Micro Service Arch

Project Duration: October 14, 2023 to October 25, 2023

Teacher : Johan Dams
Subject : Intelligent Cloud Applications 
Name : Naimul Hassan Noor (2204084)


Project Team (06):
•	Project Manager: Naimul Hassan Noor (2204084)
1.	Developers: Md Foysal Kober, Tuan Hoang, Srinivasa and Naimuna Manzoor Anna

Table of Contents
•	Summary
•	Project Objectives
•	API Selection
•	Technical Architecture
•	Implementation
•	Testing
•	Challenges Faced
•	Results
•	Conclusion
•	Future Enhancements












1. Summary
The objective of this project is to create a multipurpose API for performing three core functions: Image-to-Text Conversion, Text-to-Speech Conversion, Text Translation. These functionalities are integrated into a single API and deployed on a Kubernetes cluster within a Minikube environment, utilizing a Load Balancer for efficient resource allocation and scaling.

 

Ui of the Application :



2. Project Objectives
•	Develop a robust API capable of handling image-to-text, text-to-speech, and text translation requests. 
•	Ensure high accuracy and performance for each function. 
•	Deploy the API using Kubernetes and a Load Balancer for scalability and redundancy. 
•	Provide comprehensive documentation for developers.

3. API Selection
The chosen APIs for this project are as follows:
•	Image-to-Text: Custom-built image recognition model.
•	Text-to-Speech: Amazon Polly.
•	Text Translation: Amazon Translate.
 
1.Image to Text: 
This app Change words in pictures into computer understandable text. Image to Text, or Optical Character Recognition (OCR), is a technology that scans images or photos containing text and converts the text into a format that computers can understand. This is really helpful for tasks like taking printed documents and making them into digital text, or for extracting text from pictures and making it searchable. Think of it like a scanner that turns images with words into editable and searchable documents. 
2.Word to Speech: 
This app reads written words and change into audioable(loud words). Word to Speech, also known as Text-to-Speech (TTS),it is a technology that takes written words and converts them into spoken words. It's like having a virtual reader that can turn text from books, articles, or any written content into spoken words. This is often used for audiobooks, accessibility for people with visual impairments, or even as a voice for things like GPS navigation. 
3.Translator:
This app changes words from one language to another. A Translator application is a tool 
that lets you convert text from one language into another. It's like having a language expert who can instantly transform text in one language, let's say English, into another language, like Spanish. This is incredibly helpful for breaking down language barriers, making international communication easier, and understanding content in languages you might not know well. Translation apps like Google Translate are good examples of this . 



4. Technical Architecture
The project's technical architecture consists of several components:
•	API Gateway: Handles incoming requests and routes them to the appropriate microservices.
•	Image-to-Text Microservice: Utilizes a custom image recognition model to extract text from images.
•	Text-to-Speech Microservice: Employs Amazon Polly for text-to-speech synthesis.
•	Text Translation Microservice: Utilizes Amazon Translate for text translation.
•	Load Balancer: Distributes incoming traffic efficiently across multiple API instances for high availability.
•	Kubernetes Cluster (Minikube): Orchestrates the deployment and scaling of API instances. 

5. Implementation
The project implementation process involved the following steps:
•	Setting up the Minikube Kubernetes cluster.
•	Developing and containerizing the Image-to-Text microservice.
•	Implementing the Text-to-Speech and Text Translation microservices using Amazon Polly and Amazon Translate.
•	Deploying the microservices on the Kubernetes cluster.
•	Configuring the Load Balancer to distribute traffic evenly.

6. Testing
Comprehensive testing was conducted to ensure the reliability and performance of the API:
•	Unit tests for each microservice to verify their individual functionality.
•	Integration tests to ensure the seamless interaction between microservices.
•	Load testing to assess performance, scalability, and load balancing efficiency.
•	User acceptance testing to ensure the API meets project requirements. 

7. Challenges Faced
Several challenges were encountered during the project:
•	Custom Image Recognition Model: Developing and fine-tuning the image recognition model for accurate text extraction.
•	Load Balancer Configuration: Configuring the Load Balancer for optimal traffic distribution.
•	Kubernetes Deployment: Managing containerized microservices within a Kubernetes cluster.
•	Security: Implementing robust security measures to protect sensitive user data. 

8. Results
The API successfully achieves its objectives:
•	Image-to-Text conversion is accurate and can handle various image formats.
•	Text-to-Speech conversion provides high-quality audio output.
•	Text Translation supports multiple languages and offers accurate translations.

9. Conclusion
The project has delivered a multipurpose API that combines image-to-text, text-to-speech, and text translation. It is a valuable tool for developers and businesses looking to automate and enhance their text and image processing capabilities.

10. Future Enhancements
In the future, we plan to enhance the API by:
•	Adding support for more languages in the Text Translation microservice.
•	Expanding the choice of text-to-speech voices and languages.
This project report summarizes the successful completion of the API integration project and outlines plans for future improvements. The API opens up numerous possibilities for text and image processing, benefiting a wide range of applications and industries.





Test api link : 

curl -X POST -H "Content-Type: application/json" -d '{"data": "I love football", "lang": "bn"}' http://translation-service:8082/translate-text


Command list : 

set env for minikube : eval $(minikube docker-env)
Run the program : python3 api.py
Build the image : docker build -t image-name . Run the image : docker run -p 80:80 image-name Minikube start : minikube start 
Run Minikube dashboard : minikube dash	board
Run the minikube tunnel : minikube tunnel
Apply the deployment file : kubectl apply -f deployment.yml (filename)
Apply the service file : kubectl apply -f services.yml (filename)
Show pod : kubectl get pods
Show service : kubectl get svc

