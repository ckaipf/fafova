import glob

negatives_fastq = (glob.glob("./tests/fixtures/negatives_fastq/*.fastq"))
positives_fastq = (glob.glob("./tests/fixtures/positives_fastq/*.fastq"))

positives_fasta_dna = (glob.glob("./tests/fixtures/positives_fasta_dna/*.fa"))
negatives_fasta_dna = (glob.glob("./tests/fixtures/negatives_fasta_dna/*.fa"))
