from pathlib import Path
from Bio import Entrez
def baixar_genoma(iden, output_folder=Path("data")/"genomes"):
    #Faz os genomas irem pra uma pasta relativa ao repositório
    output_folder.mkdir(parents=True, exist_ok=True)
    filename= output_folder/f"{iden}.fasta"
    
    #Acessando o Entrez
    Entrez.email="computandocombiopy@gmail.com"

    #Checo se o arquivo fasta existe, se não ele o cria
    if not filename.exists():
        #Baixa o arquivo .fasta (funciona para GenBank e RefSeq)
        stream= Entrez.efetch(
            db="nucleotide",id=iden, rettype="fasta", retmode="text"
        )
        data = stream.read()
        #Checa se data tá vazio ou não
        if not data:
            print("Error: Resposta vazia do NCBI.")
        else:
            with open(filename, "w") as output:
                output.write(data)
        print(f"Salvo em {filename}")
