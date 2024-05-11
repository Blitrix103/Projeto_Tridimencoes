try:
  import vpython  # Tentar importar a biblioteca VPython
except ImportError:  # Se a importação falhar (erro de importação)
  print("Biblioteca VPython não encontrada!")
  
  # Instalar a biblioteca VPython usando o PIP
  import subprocess
  subprocess.run(["pip", "install", "vpython"])

  # Importar a biblioteca VPython novamente após a instalação
  import vpython
  print("Biblioteca VPython instalada com sucesso!")

import google.generativeai as genai

genai.configure(api_key="AIzaSyCBcDGdBKn9Pvcj4M-99hF42JdPR1V5PQU")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Quero cria um programa com o API do gemini que tranforma os pedidos do usuario em codigos python e gere um objeto 3D pronto, você pode me ajudar"]
  },
  {
    "role": "model",
    "parts": ["Criar um programa que traduz pedidos em código Python para gerar objetos 3D é um projeto ambicioso, mas podemos dividir em etapas.  \n\n**Desafios:**\n\n* **Compreensão da Linguagem Natural:** Interpretar as solicitações dos usuários em linguagem natural (ex: \"Crie um cubo vermelho de 5cm\") é um desafio complexo.\n* **Tradução para Código Python:** Transformar a intenção em código Python que utilize uma biblioteca 3D (como PyOpenGL, Blender API) requer um sistema de regras e mapeamento sofisticado.\n* **Geração de Objeto 3D:** Garantir que o código gerado crie o objeto 3D desejado pelo usuário com a forma, cor, textura, etc. corretas exige um conhecimento profundo da biblioteca escolhida.\n\n**Etapas para o Desenvolvimento:**\n\n1. **Definir Escopo:**\n    * Limitar os tipos de objetos 3D: Comece com formas básicas como cubos, esferas e cilindros.\n    * Simplificar as solicitações:  \"Crie um cubo vermelho\" em vez de \"Crie um cubo vermelho com textura de madeira\".\n    * Escolher uma biblioteca 3D: PyOpenGL é uma boa opção para começar.\n\n2. **Criar um Interpretador de Comandos:**\n    * Utilize uma biblioteca de Processamento de Linguagem Natural (PNL) como NLTK ou SpaCy.\n    * Crie regras para identificar palavras-chave como \"cubo\", \"vermelho\", \"5cm\" e mapear para parâmetros do código Python.\n\n3. **Gerar Código Python:**\n    * Utilize templates de código Python para as formas básicas.\n    * Substitua os parâmetros do template com base na interpretação das palavras-chave.\n    * O código deve usar a biblioteca 3D escolhida para criar o objeto.\n\n4. **Executar o Código e Visualizar o Objeto:**\n    * Execute o código Python gerado.\n    * A biblioteca 3D deve renderizar o objeto para visualização.\n\n**Exemplo Simplificado (usando PyOpenGL):**\n\n```python\nimport OpenGL.GL as gl\nimport OpenGL.GLUT as glut\nimport OpenGL.GLU as glu\n\n# Interpretação do comando (simplificado)\ncomando = \"crie um cubo azul\"\nforma = \"cubo\"\ncor = \"azul\"\n\n# Código Python (template)\nif forma == \"cubo\":\n  glut.glutSolidCube(1) # Tamanho padrão\n  gl.glColor3f(0, 0, 1) # Define a cor azul\n```\n\n**Considerações Adicionais:**\n\n* **API da Gemini:** A API da Gemini, se for a interface de usuário, precisa ser integrada ao interpretador de comandos e ao gerador de código.\n* **Escalabilidade:** Para lidar com solicitações complexas, você precisará de uma base de conhecimento robusta e um sistema de regras mais avançado.\n* **Testes e Feedback:** É crucial testar o programa com diversos pedidos e refinar a interpretação e geração de código com base no feedback do usuário.\n\nLembre-se de que este é um projeto desafiador, mas com pesquisa, planejamento e desenvolvimento cuidadoso, você pode criar um programa que traduza pedidos em código Python para gerar objetos 3D."]
  },
])
print('Agora posso projetar objetos simples para você, o que dezeja?')
User = input('Pedido: ')
User = User + '. Use apenas a função vpython para criar o objeto e não pare a execução automaticamentemesa, Quero tambem que me apresentes apenas o codigo python e nada mais, nem se quer esse termo: ```python; apenas linhas de codigo'
convo.send_message(User)
# print(convo.last.text)

def criar_arquivo(nome_arquivo, conteudo):
  # """
  # Função para criar um novo arquivo Python no mesmo diretório.

  # Argumentos:
  #   nome_arquivo (str): Nome do arquivo a ser criado.
  #   conteudo (str): Conteúdo do arquivo Python a ser escrito.

  # Retorno:
  #   None
  # """

  try:
    with open(nome_arquivo, "w") as arquivo:
      arquivo.write(conteudo)
  except Exception as erro:
    print(f"Erro ao compilar o objecto, porfavor tente novamente: {erro}")

# Exemplo de uso
nome_arquivo = "obj.py"
conteudo = convo.last.text

criar_arquivo(nome_arquivo, conteudo)
print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

import subprocess

def executar_arquivo(nome_arquivo):
  # """
  # Função para executar um arquivo Python no mesmo diretório.

  # Argumentos:
  #   nome_arquivo (str): Nome do arquivo Python a ser executado.

  # Retorno:
  #   None
  # """

  try:
    subprocess.run(["python", nome_arquivo])
  except Exception as erro:
    print(f"Erro ao executar arquivo: {erro}")

# Exemplo de uso
nome_arquivo = "obj.py"

executar_arquivo(nome_arquivo)
print(f"Arquivo '{nome_arquivo}' executado com sucesso!")



