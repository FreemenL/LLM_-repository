from pathlib import Path

class TextLoader:
    def __init__(self, file_path: str | Path, encoding: str = "utf-8"):
        self.file_path = Path(file_path)
        self.encoding = encoding

    def load(self) -> list[Document]:
        return [
            Document(
                page_content=self.file_path.read_text(encoding=self.encoding),
                metadata={"source": str(self.file_path)},
            )
        ]
# if __name__ == "__main__":

path = Path(__file__).parent / "text" / "example.txt"
loader = TextLoader(file_path=path, encoding="utf-8")
documents = loader.load()

print(len(documents))
print(documents[0])

    # print(TextLoader)
