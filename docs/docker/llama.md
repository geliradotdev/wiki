## llama3.2


# run command
docker run -d \
  --name ollama \
  --restart unless-stopped \
  -p 11434:11434 \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/ai/ollama:/root/.ollama \
  ollama/ollama

# Then install/pull Llama 3.2 inside the container
docker exec -it ollama ollama pull llama3.2

# Test it:
docker exec -it ollama ollama run llama3.2