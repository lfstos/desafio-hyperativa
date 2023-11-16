## Setup

### Antes de começar, certifique-se de ter o Python e o pip instalados. Em seguida, siga estas etapas:

### Clone o repositório:

```bash
   git clone https://github.com/lfstos/desafio-hyperativa
```

### Crie e ative um ambiente virtual:
```bash
python -m venv .venv
```

### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Configure o banco de dados:
```bash
python manage.py migrate
```

### Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

### Agora, seu ambiente está configurado e pronto para uso.

## Executando o projeto

## Para usar este projeto, siga as seguintes etapas:

### 1. Execute o servidor de desenvolvimento:

```bash
   python manage.py runserver
```

### Abra o navegador e vá para http://localhost:8000/api/

# Endpoints

- **Listagem de Cartões:**
  - Método: GET
  - Endpoint: /api/cartoes/

- **Detalhes do Cartão:**
  - Método: GET
  - Endpoint: /api/cartoes/{numero_cartao}/

- **Criação de Cartão:**
  - Método: POST
  - Endpoint: /api/cartoes/