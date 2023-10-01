# GitaGPT
This project is a chatbot that provides answers and guidance based on the teachings of The Bhagavad Gita. It utilizes Meta’s Llama 2 model to generate meaningful responses to user queries.

# How to run

1.    Ensure you have the chat.sh bash script available in your system.

2.   Navigate to the directory containing the script.

3.   Make the bash file executable by running:

```bash
chmod +x chat.sh
```

4.   Run the bash file:

```bash
./chat.sh
```
This will start the application.

5.   Access the chatbot through your web browser at
```bash
http://localhost:8000/
```

# Work done
- Developed a chatbot application using the advanced Llama 2 model accessible via Hugging Face.
- Implemented a user-friendly UI using Chainlit.
- Containerized the application with Docker for easy deployment and management.
- Set up a GitHub Actions workflow for automated image building and pushing to Docker Hub upon each push event.
- Created a convenient bash script (chat.sh) to streamline container execution and provide user access instructions.
- Established a Kubernetes manifest file (development.yaml) to facilitate web server hosting.

  




