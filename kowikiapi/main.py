import os
from typing import List
from pathlib import Path

import wikipediaapi
import typer

import kowikiapi

app = typer.Typer(help="Korea Wikipedia dumping api")


def dump(name: str, sentences: List[str], save_dir: str) -> None:
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    name = name.replace("/", "_")
    with open(save_dir / f"{name}.txt", "w") as f:
        for sentence in sentences:
            f.write(sentence)
            f.write("\n")


def extarct_sentences(lines: List[str], min_line_length: int) -> List[str]:
    import kss

    sentence_list = map(kss.split_sentences, lines)
    sentences = []
    for sentence in sentence_list:
        for line in sentence:
            if len(line) > min_line_length:
                sentences.append(line)
    return sentences


@app.command()
def version() -> None:
    """Show version"""
    typer.secho(kowikiapi.__version__)


@app.command()
def extract(
    name: str = typer.Option(..., help="Name to extract"),
    save_dir: str = typer.Option(..., help="Path to save extracted wiki"),
    kss: bool = typer.Option(False, is_flag=True, help="Path to save extracted wiki"),
    line_length: int = typer.Option(
        10, help="Skip sentence which is smaller than given length"
    ),
    split_name: bool = typer.Option(False, is_flag=True, help="Split name with comma"),
):
    wiki_ko = wikipediaapi.Wikipedia("ko")
    if split_name:
        names = name.split(",")
    else:
        names = [name]
    for name in names:
        page = wiki_ko.page(name)
        if not page.exists():
            print(f"{name} is not proper article name.")
            continue
        lines = [page.text]
        if kss:
            lines = extarct_sentences(lines, line_length)
        dump(name, lines, save_dir)


@app.command()
def lines(
    path: str = typer.Option(..., help="Path to count lines"),
    line_length: int = typer.Option(
        10, help="Skip sentence which is smaller than given length"
    ),
):
    import kss

    path = Path(path)
    total_length = 0
    for file_path in path.glob("*.txt"):
        sentences = []
        with open(file_path, "r") as file_reader:
            lines = file_reader.readlines()
            sentence_list = map(kss.split_sentences, lines)
            for sentence in sentence_list:
                for line in sentence:
                    if len(line) > line_length:
                        sentences.append(line)
        print(f"{file_path}:", len(sentences))
        total_length += len(sentences)
    print("Total sentence length:", total_length)


def entry_point():
    app()


if __name__ == "__main__":
    app()
