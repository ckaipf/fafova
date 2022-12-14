import sys
import os
import typer
from typing import List, Union, Tuple, Dict

from Bio import SeqIO

app = typer.Typer()

def additional_record_validation(
    field_1: str,
    field_2: str,
    field_3: str,
    field_4: str,
) -> Union[str, bool]:
    if any(ch.upper() not in ["A", "T", "G", "C"] for ch in field_2):
        raise ValueError("Field 2 contains non sequence characters")

def try_formats(
    path: str
    ) -> Tuple[bool, str, List[Exception]]:
    """
    Try available fastq formats of SeqIO.
    """
    acc = []
    for format in ["fastq-illumina", "fastq-solexa", "fastq-sanger"]:
        try:
            with open(path) as handle:
                if any(True for _ in SeqIO.parse(handle, format)):
                    acc.append((True, format, []))
        except Exception as e:
            acc.append((False, format, [e]))
    return acc

def parse_fastq(
    path: str,
    ) -> Dict[str, List[Exception]]:
    """
    Try to parse a fastq file using SeqIO.
    """
    acc = dict()
    for is_valid,format,messages in try_formats(path):
        if is_valid:
            with open(path) as handle:
                try:
                    for record in SeqIO.parse(handle, format):
                        additional_record_validation(record.id, record.seq, record.description, record.letter_annotations["phred_quality"])
                except Exception as e:
                        messages.append(e)
        acc[format] = messages
    return(acc)

@app.command()
def fastq_validation(
    path: str
    ):
    """
    Validate fastq file with SeqIO.
    """
    if os.path.getsize(path) == 0:
        return sys.exit(1)

    parsed = parse_fastq(path)

    for _,messages in parsed.items():
        if not messages:
            return sys.exit(0)
    
    return sys.exit(1)
