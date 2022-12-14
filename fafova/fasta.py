import sys
import os
import typer
from typing import List, Union, Tuple, Dict

from Bio import SeqIO

from .alphabets import DNA, RNA, PROTEIN

app = typer.Typer()

def additional_record_validation(
    field_1: str,
    field_2: str,
    field_3: str,
) -> Union[str, bool]:
    if any(ch.upper() not in chars for ch in field_2):
        raise ValueError("Field 2 contains non sequence characters")

def try_formats(
    path: str
    ) -> Tuple[bool, str, List[Exception]]:
    """
    Try available fasta formats of SeqIO.
    """
    acc = []
    for format in ["fasta"]:
        try:
            with open(path) as handle:
                if any(True for _ in SeqIO.parse(handle, format)):
                    acc.append((True, format, []))
        except Exception as e:
            acc.append((False, format, [e]))
    return acc

def parse_fasta(
    path: str,
    ) -> Dict[str, List[Exception]]:
    """
    Try to parse a fasta file using SeqIO.
    """
    acc = dict()
    for is_valid,format,messages in try_formats(path):
        if is_valid:
            with open(path) as handle:
                try:
                    for record in SeqIO.parse(handle, format):
                        print(record)
                        additional_record_validation(record.name, record.seq, record.description)
                except Exception as e:
                        messages.append(e)
        acc[format] = messages
    return(acc)

@app.command()
def fasta_validation(
    path: str,
    alphabet: List[str] = "DNA",
    ):
    """
    Validate fasta file with SeqIO.
    """
    if os.path.getsize(path) == 0:
        return sys.exit(1)
    
    global chars
    if alphabet == "DNA":
        chars = DNA 
    if alphabet == "RNA":
        chars = RNA   
    if alphabet == "PROTEIN":
        chars = PROTEIN   
    

    parsed = parse_fasta(path)
    print(parsed)
    for _,messages in parsed.items():
        if not messages:
            return sys.exit(0)
    
    return sys.exit(1)
