#!/bin/bash

# 1. Cria a pasta .streamlit (se não existir)
mkdir -p .streamlit

# 2. Cria o ficheiro secrets.toml lendo as variáveis de ambiente
#    com os nomes exatos que você definiu no .env / secrets.toml
#    (Ex: $client_id, $client_secret)

echo "[auth]" > .streamlit/secrets.toml
echo "client_id = \"$client_id\"" >> .streamlit/secrets.toml
echo "client_secret = \"$client_secret\"" >> .streamlit/secrets.toml
echo "redirect_uri = \"$redirect_uri\"" >> .streamlit/secrets.toml
echo "cookie_secret = \"$cookie_secret\"" >> .streamlit/secrets.toml
echo "server_metadata_url = \"$server_metadata_url\"" >> .streamlit/secrets.toml

# 3. Finalmente, executa o comando principal do Streamlit
streamlit run app.py --server.port $PORT --server.enableCORS=false --server.enableXsrfProtection=false