import typer

from .fastq import app as fastq_validation

app = typer.Typer()
app.add_typer(fastq_validation, name="fastq_validation")

@app.callback()
def main():
    """
    Format validation.
    """

if __name__ == "__main__":
    app()