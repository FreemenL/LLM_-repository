from langchain_community.document_loaders import PyPDFLoader

print(PyPDFLoader)
path = "./text/"

loader = PyPDFLoader(file_path=path+'刘夏江的简历.pdf')

documents = loader.load()

print(len(documents))


for item,doc in enumerate(documents):
    print(f"文档片段{item+1}内容为\n{doc}\n")
    print("================")