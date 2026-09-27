from langchain_community.document_loaders import Docx2txtLoader

path = "./text/"

loader = Docx2txtLoader(file_path=path+'尚硅谷大模型技术之Python2.0.docx');

documents = loader.load()

print(len(documents))

for item,doc in enumerate(documents):
    print(f"文档片段{item + 1}内容为\n{doc}\n")
    print("================")