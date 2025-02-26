import requests
from bs4 import BeautifulSoup
import re

def validar_url(url):
    """Valida se a URL está em um formato correto."""
    padrao = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$', re.IGNORECASE)
    return bool(padrao.match(url))

def extrair_titulo(url):
    """Extrai o título de uma página web a partir da URL fornecida."""
    if not validar_url(url):
        return "URL inválida. Verifique o formato e tente novamente."
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
        resposta.encoding = resposta.apparent_encoding  # Ajusta a codificação se necessário
        
        soup = BeautifulSoup(resposta.text, 'html.parser')
        titulo = soup.title.string if soup.title else "Título não encontrado"
        return titulo.strip()
    except requests.exceptions.MissingSchema:
        return "Erro: Esquema de URL ausente. Use 'http://' ou 'https://'."
    except requests.exceptions.ConnectionError:
        return "Erro: Não foi possível conectar ao servidor."
    except requests.exceptions.Timeout:
        return "Erro: A requisição excedeu o tempo limite."
    except requests.exceptions.HTTPError as e:
        return f"Erro HTTP: {e}"
    except requests.exceptions.RequestException as e:
        return f"Erro inesperado: {e}"

if __name__ == "__main__":
    url = input("Digite a URL da página: ")
    titulo = extrair_titulo(url)
    print(f"Título da página: {titulo}")
