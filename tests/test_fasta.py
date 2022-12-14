from fafova.fasta import fasta_validation
import pytest
from fixtures import negatives_fasta_dna, positives_fasta_dna

def test_fasta_validation():
    for file in negatives_fasta_dna:
        with pytest.raises(SystemExit) as e:
            fasta_validation(file)
        assert e.value.code == 1

    for file in positives_fasta_dna:
         with pytest.raises(SystemExit) as e:
            fasta_validation(file, alphabet="DNA")
         assert e.value.code == 0
