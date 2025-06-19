from pathlib import Path 
import sys
from collections import defaultdict

#Obtendo todos arquivos da pasta genomes (retorna uma lista com objetos path)
def obtendo_fasta(fasta_dir: Path) -> list[Path]:
  #Checando se o diretório existe ou não
  if not fasta_dir.exists():
    raise FileNotFoundError(f"Diretório de arquivos FASTA não encontrado: {fasta_dir}")
#verificação dupla agora de se é realmente um diretório e não um arquvio
  if not fasta_dir.is_dir():
    raise NotADirectoryError(f"O caminho não é um diretório: {fasta_dir}")
  return list(fasta_dir.glob('*.fasta'))+list(fasta_dir.glob('*.FASTA'))

  
def calculo_dist(fasta_file: Path):
  #inicializo como defaultdict (me ajuda a manejar o dicionário, execução
  #+rápida)
  contador_bases=defaultdict(int)
  total_bases=0
  """A função calcula a porcentagem de bases em uma sequência de RNA.
  Os retornos são (percentual_gc, {'A':x%, 'U':y%, 'C':z%, 'G':w%})
  """
  #Abro o arquivo e chamo de f
  with open(fasta_file, 'r') as f:
    for linha in f:
      if linha.startswith('>'):
          continue
    #Por que strip() e upper? Retiro qualquer espaço ou caracter de linha nova
    #Converto tudo pra maiúsculo.
      for base in linha.strip().upper():
        #PARA RNA PELO AMOR
        if base in 'ACGUT':
          contador_bases[base]+=1
          total_bases+=1

  base_percentuais={
    base:(count/total_bases)*100 
    for base, count in contador_bases.items()
  }

  perc_gc= base_percentuais.get('G', 0) + base_percentuais.get('C',0)
  
  return perc_gc, base_percentuais
  
def calculando_distribuicoes():
  porcentagensCG={}
  lista_porcentagens={}
  #Obtendo o caminho em que esse código está sendo executado
  raiz_projeto = Path(__file__).parent

  #Encontro o caminho para a pasta genomes que tem os arquivos .fasta
  fasta_dir= raiz_projeto / "genomes"

  try: 
    #Obtenho todos os arquivos que vem do diretório 
    fasta_files=obtendo_fasta(fasta_dir)

    #Quero saber se eu puxei os arquivos do diretório:
    if not fasta_files:
      print(f"Sem arquivos fasta em {fasta_dir}")
      #Sai do código prematuramente (não tinha nada, tem que sair)
      return
    #Achei arquivos!!
    print(f"Encontrados {len(fasta_files)} arquivos .fasta")

    #Percorro os arquivos e adiciono nos dicionários um par
    #código do virus/porcentagemC e codigo do virus/lista_porcentagens
    for fasta_file in fasta_files:
      #perc_cg tem a porcentagem de CG e lista_perc tem as porcentagens de cada
      #par de base
      perc_gc, lista_perc=calculo_dist(fasta_file)
      porcentagensCG[fasta_file.stem]=perc_gc
      lista_porcentagens[fasta_file.stem]=lista_perc

  except Exception as e:
    print(f"Erro {str(e)}", file=sys.stderr)
    sys.exit(1)
      
  return porcentagensCG, lista_porcentagens

