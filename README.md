![insert some_code here](https://github.com/user-attachments/assets/33404899-7018-44c5-949e-37921559ec2f)

# 🧬 Computando Semelhança Genética Viral 🧬

Projeto realizado para a diciplina de Práticas em Ciência de Dados no primeiro semestre de 2025 do curso de Ciência e Tecnologia, Ilum Escola de Ciência.

A ideia para o projeto surgiu do desejo de relacionar conceitos estudados em outras áreas do conhecimento com as funcionalidades do Python estudadas durante o primeiro semestre. Por esse motivo, optou-se por aplicar as ideias de matrizes, processamento de strings e composição de gráficos para comparar as semelhanças e diferenças entre genomas de vírus já catalogados. 

O objetivo do programa é automatizar a análise e o estudo genômico dos arbovírus, vírus transmitidos por artrópodes e que, por esse motivo, afetam especialmente regiões tropicais, como a América do Sul. A análise da estrutura genética desses vírus pode ajudar a entender sua história evolutiva, detectar variantes, estabelecer por onde ele passou e atualizar vacinas, por exemplo.

# !["Badge Ilum"](https://img.shields.io/badge/Ilum%20-%20purple) !["Badge Satus"](https://img.shields.io/badge/Status%20-%20Em_Desenvolvimento%20-%20orange)

# 🛠️ Ferramentas Utilizadas 🛠️

### IA

Utilizamos Inteligência Artificial para compreender as funcionalidades do Biopython e como aplicá-las em nosso projeto.

### Bibliotecas e Módulos

- [Biopython](https://biopython.org/) (Entrez, SeqIO, AlignIO)
- [Subprocess](https://docs.python.org/3/library/subprocess.html)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Numpy](https://numpy.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Ipywidgets](https://ipywidgets.readthedocs.io/en/stable/)
- [IPython.display](https://ipython.readthedocs.io/en/8.26.0/api/generated/IPython.display.html)

### NCBI

O [NCBI](https://www.ncbi.nlm.nih.gov/) (Centro Nacional de Informação Biotecnológica) é uma divisão da Biblioteca Nacional de Medicina dos Estados Unidos (U.S. National Library of Medicine), que por sua vez faz parte dos Institutos Nacionais de Saúde (NIH - National Institutes of Health).

Ele é responsável por manter diversos recursos biológicos, incluindo o GenBank, um repositório público de sequências de nucleotídeos e suas anotações. Este banco de dados é amplamente utilizado em bioinformática para análise de genomas, sendo uma fonte essencial de dados para ferramentas de busca, comparação e alinhamento de sequências genéticas.

### Muscle

O [Muscle](https://www.ncbi.nlm.nih.gov/) (Multiple Sequence Comparison by Log-Expectation) é um software de computador para alinhamento de múltiplas sequências de proteínas e nucleotídeos, sendo licenciado como domínio público.

O alinhamento de sequências é o processo de comparar duas sequências (no caso, de nucleotídeos) para observar seu nível de identidade. O alinhamento
entre duas sequências pode ser feito de forma global ou local. Quando global, comparamos uma sequência, ao longo de toda sua extensão, mas local se a comparação é apenas em pequenas regiões. Nesse contexto, MUSCLE é capaz de comparar genomas de ambas as formas, retornando um score de alinhamento, que é a soma dos pontos de similaridades, diferenças e abertura e extensão de falhas.

O alinhamento é considerado simples quando apenas duas sequências são alinhadas, e múltipla quando três ou mais devem ser alinhadas entre si. No caso, a depender das entradas fornecidas pelo usuário, alinhamento simples ou múltiplo será realizado.


#### Versão do Python
- Python 3.12.7


# 💻 Instalação e Instruções 💻

### Instalação do Muscle
Para o funcionamento desse programa, é essencial que o usuário tenha instalado em sua máquina o software do Muscle. Toda a documentação associada a ele se encontra no seguinte link:

[Documentação MUSCLE Completa](https://muscle3.readthedocs.io/en/latest/index.html)

Além do site oficial, encontramos um repositório do GitHub que contém todas as informações sobre o Muscle e todos os arquivos necessários para sua instalação. Os arquivos estão reunidos na seguinte [pasta](https://github.com/rcedgar/muscle/releases/tag/v5.3). Basta encontrar o executável que possui as especificações desejadas e selecioná-lo. A instalação será iniciada imediatamente.

⚠️ IMPORTANTE ⚠️

É importante ressaltar que, para o funcionamento correto de todas as funções, é preciso que o software Muscle e o código a ser executado estejam salvos no mesmo diretório, ou seja, é preciso que o usuário salve ambos os arquivos em uma mesma pasta em seu computador. Para facilitar esse processo, deixamos disponível uma pasta que já contém ambos os arquivos. Abaixo estão as instruções de como realizar este processo.

### Instalação do Código
O código principal para a execução deste projeto se encontra neste repositório do GitHub, na pasta [nome da pasta](link). Caso o usuário já tenha realizado a instalação do Muscle previamente, é possível baixar apenas o [código principal](link). Caso contrário, é recomendado que o usuário baixe a pasta completa.

Ao realizar o download, é possível perceber que o arquivo é um Jupyter Notebook, ou seja, deve ser rodado em programas que possuam um Jupyter Kernel. Durante a realização do projeto, foram utilizados o JupyterLab e o Visual Studio Code, sendo os mais recomendados para a execução, uma vez que os testes já foram realizados neles. Além disso, é preciso que o usuário tenha instalado todas as bibliotecas citadas anteriormente em seu computador.

### Instalação das Bibliotecas
Outro ponto que exige atenção antes da execução do código tem relação com as bibliotecas que serão utilizadas. Em tópicos anteriores, tais ferramentas já foram citadas, incluindo também, o link para a página de cada uma delas na internet. Para que o código seja executado corretamente, o usuário deve verificar se já possui todas essas bibliotecas instaladas em seu dispositivo. Caso alguma delas não esteja, o usuário deverá criar uma nova célula, digitar **pip install** *(nome da biblioteca)* e executar. Por exemplo, para instalar a biblioteca Seaborn, digita-se *pip install seaborn*

# 👥 Desenvolvedores do Projeto 👥

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/106536784?v=4" width=115><br><sub>😄Bruna Guedes Pereira😄</sub>](https://github.com/Bruna-guedes09)

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/173375194?v=4" width=115><br><sub>😎Jonatas Rafael de Oliveira Melo😎</sub>](https://github.com/jonatas727)

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/195492158?v=4" width=115><br><sub>🍂Luiza Davoli🍂</sub>](https://github.com/Luiza160)

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/88594280?v=4" width=115><br><sub>🐳Matheus Macedo do Nascimento🐳</sub>](https://github.com/matheusMNa)

Agradecimento especial aos professores da matéria de Práticas em Ciência de Dados, por todo o aprendizado durante o semestre e a colaboração para a realização desse projeto:

📍Professor Daniel Roberto Cassar

📍Professor James Moraes de Almeida

📍Professor Leandro Nascimento Lemos
