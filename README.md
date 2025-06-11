![insert some_code here](https://github.com/user-attachments/assets/33404899-7018-44c5-949e-37921559ec2f)

# 🧬 Computando Semelhança Genética Viral 🧬

Projeto realizado para a diciplina de Práticas em Ciência de Dados no primeiro semestre de 2025 do curso de Ciência e Tecnologia, Ilum Escola de Ciência.

A ideia para o projeto surgiu do desejo de relacionar conceitos estudados em outras áreas do conhecimento com as funcionalidades do Python estudadas durante o primeiro semestre. Por esse motivo, optou-se por aplicar as ideias de grafos, matrizes e processamento de strings para comparar as semelhanças e diferenças entre genomas de vírus já catalogados. 

# !["Badge Ilum"](https://img.shields.io/badge/Ilum%20-%20purple) !["Badge Satus"](https://img.shields.io/badge/Status%20-%20Em_Desenvolvimento%20-%20orange)

# ⭐ Objetivo ⭐

O objetivo do programa é automatizar a análise e o estudo genômico dos arbovírus, vírus transmitidos por artrópodes e que, por esse motivo, afetam especialmente regiões tropicais, como a América do Sul.

A análise da estrutura genética dos vírus pode ajudar a entender a história evolutiva de um vírus, detectar suas variantes, estabelecer por onde ele passou e atualizar vacinas, por exemplo.

# 💻 Instalação e Instruções 💻

# 🛠️ Ferramentas Utilizadas 🛠️

IA

Utilizamos Inteligência Artificial para compreender as funcionalidades do Biopython e como aplicá-las em nosso projeto.


Biopython

É um conjunto de ferramentas gratuitas para computação biológica em Python. É projeto membro da Open Bioinformatics Foundation (OBF), com repositório no GitHub (https://github.com/biopython).


NCBI

O NCBI (Centro Nacional de Informação Biotecnológica) é uma divisão da Biblioteca Nacional de Medicina dos Estados Unidos (U.S. National Library of Medicine), que por sua vez faz parte dos Institutos Nacionais de Saúde (NIH - National Institutes of Health).

Ele é responsável por manter diversos recursos biológicos, incluindo o GenBank, um repositório público de sequências de nucleotídeos e suas anotações. Este banco de dados é amplamente utilizado em bioinformática para análise de genomas, sendo uma fonte essencial de dados para ferramentas de busca, comparação e alinhamento de sequências genéticas.


Entrez

O Entrez é o sistema de busca e integração de dados do NCBI, que permite o acesso a diversos bancos de dados biológicos, como o GenBank, PubMed, Gene, entre outros.

Neste projeto, utilizamos o Entrez para acessar e baixar os genomas de variantes virais diretamente do NCBI. Isso foi feito por meio do módulo Bio.Entrez, fornecido pelo pacote Biopython, que oferece uma interface programática para as funcionalidades disponibilizadas pelo NCBI.

Mais especificamente, acessamos o banco de dados GenBank para obter as sequências genômicas necessárias para análise.


Muscle

Multiple Sequence Comparison by Log-Expectation é um software de computador para alinhamento de múltiplas sequências de proteínas e nucleotídeos, sendo licenciado como domínio público.

O alinhamento de sequências é o processo de comparar duas sequências (no caso, de nucleotídeos) para observar seu nível de identidade. O alinhamento
entre duas sequências pode ser feito de forma global ou local. Quando global, comparamos uma sequência, ao longo de toda sua extensão, mas local se a comparação é apenas em pequenas regiões. Nesse contexto, MUSCLE é capaz de comparar genomas de ambas as formas, retornando um score de alinhamento, que é a soma dos pontos de similaridades, diferenças e abertura e extensão de falhas.

O alinhamento é considerado simples quando apenas duas sequências são alinhadas, e múltipla quando três ou mais devem ser alinhadas entre si. No caso, a depender das entradas fornecidas pelo usuário, alinhamento simples ou múltiplo será realizado.

SeqIO

É um módulo da biblioteca Biopython para ler e escrever sequências de DNA, RNA ou proteínas a partir de arquivo como FASTA, GenBank ou EMBL, além de converter um formato para outro, lidando com arquivos contendo uma ou mais sequências representadas como objetos SeqRecord.


AlignIO

É um módulo de Biopython que fornece uma interface de entrada e saída de alinhamento de sequência, lidando com arquivos que contêm um ou mais alinhamentos de sequência representados como objetos Alignment.

Subprocess

O módulo subprocess é parte da biblioteca padrão do Python. É usado para executar comandos do sistema operacional a partir do seu script Python. No caso, foi utilizado para chamar o MUSCLE.exe .

matplotlib.pyplot

O módulo pyplot, parte da biblioteca Matplotlib, é utilizado para criar gráficos e visualizações em Python. 

Seaborn

É uma biblioteca de visualização de dados em python que deixa os gráficos mais profissionais e informativos, usando como base o matplotlib. No caso, foi utilizado para gerar, com base na matriz de similaridade, um heatmap (gráfico em forma de tabela colorida para visualizar valores numéricos, onde as cores representam os números).

Numpy

NumPy (Numerical Python) é uma biblioteca do Python usada para fazer cálculos matemáticos e trabalhar com arrays (matrizes/vetores). No caso, utilizamos NumPy para  criar a matriz de similaridade entre genomas antes de exibir no heatmap com seaborn.


Plopy






# 👥 Desenvolvedores do Projeto 👥

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/106536784?v=4" width=115><br><sub>😄Bruna Guedes Pereira😄</sub>](https://github.com/Bruna-guedes09)

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/173375194?v=4" width=115><br><sub>😎Jonatas Rafael de Oliveira Melo😎</sub>](https://github.com/jonatas727)

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/195492158?v=4" width=115><br><sub>🍂Luiza Davoli🍂</sub>](https://github.com/Luiza160)

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/88594280?v=4" width=115><br><sub>🐳Matheus Macedo do Nascimento🐳</sub>](https://github.com/matheusMNa)

Agradecimento especial aos professores da matéria de Práticas em Ciência de Dados, por todo o aprendizado durante o semestre e a colaboração para a realização desse projeto:

📍Professor Daniel Roberto Cassar

📍Professor James Moraes de Almeida

📍Professor Leandro Nascimento Lemos


#### Referências:
Sequenciamento genômico: no rastro do vírus. Disponível em: <https://agencia.fiocruz.br/sequenciamento-genomico-no-rastro-do-virus>. Acesso em: 11 jun. 2025.

Accessing NCBI’s Entrez databases — Biopython 1.85 documentation. Disponível em: <https://biopython.org/docs/latest/Tutorial/chapter_entrez.html#chapter-entrez>. Acesso em: 11 jun. 2025.

NATIONAL CENTER FOR BIOTECHNOLOGY INFORMATION. Our Mission - NCBI. Disponível em: <https://www.ncbi.nlm.nih.gov/home/about/mission/>.

‌DOS, C. GenBank. Disponível em: <https://pt.wikipedia.org/wiki/GenBank>. Acesso em: 11 jun. 2025.

‌BIOPYTHON. Biopython · Biopython. Disponível em: <https://biopython.org/>.

Biopython Documentation — Biopython 1.85 documentation. Disponível em: <https://biopython.org/docs/latest/index.html#>. Acesso em: 11 jun. 2025.

‌Cock, P. J. A., Antao, T., Chang, J. T., Chapman, B. A., Cox, C. J., Dalke, A., Friedberg, I., Hamelryck, T., Kauff, F., Wilczynski, B., & de Hoon, M. J. L. (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics, 25(11), 1422–1423.

‌OPENAI. ChatGPT (versão GPT-4) [ferramenta de inteligência artificial]. Disponível em: https://chat.openai.com/. Acesso em: 11 jun. 2025.

WIKIPEDIA CONTRIBUTORS. Sequence alignment. Disponível em: <https://en.wikipedia.org/wiki/Sequence_alignment>.

WIKIPEDIA CONTRIBUTORS. MUSCLE (alignment software).

INTRODUÇÃO, 3. 1. Alinhamento de Seqüências. Disponível em: <https://professor.pucgoias.edu.br/SiteDocente/admin/arquivosUpload/18497/material/Cap.%203%20Alinhamento%20de%20sequ%C3%AAncias.pdf>. Acesso em: 11 jun. 2025.

The module for multiple sequence alignments, AlignIO. Disponível em: <https://biopython.org/wiki/AlignIO>. Acesso em: 11 jun. 2025.

Introduction to NumPy. Disponível em: <https://www.w3schools.com/python/numpy/numpy_intro.asp>. Acesso em: 11 jun. 2025.



Edgar, R. C. (2004). MUSCLE: a multiple sequence alignment method with reduced time and space complexity. BMC Bioinformatics, 5, 113. 

