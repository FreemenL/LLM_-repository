from langchain_community.document_loaders import UnstructuredMarkdownLoader

loader = UnstructuredMarkdownLoader(
    "./安全.md",
    encoding="utf-8",
    mode="single"
)

docs = loader.load()
for doc in docs:
    print(doc.page_content,end="\n=======================\n")