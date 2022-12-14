from fafova.fastq import fastq_validation
import pytest
from fixtures import negatives_fastq, positives_fastq

def test_regify_file():
    for file in negatives_fastq:
        with pytest.raises(SystemExit) as e:
            fastq_validation(file)
        assert e.value.code == 1

    for file in positives_fastq:
         with pytest.raises(SystemExit) as e:
            fastq_validation(file)
         assert e.value.code == 0
