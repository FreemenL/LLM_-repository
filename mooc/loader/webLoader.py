from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_path="http://www.baidu.com")

documents = loader.load()

print(len(documents))
print(documents[0])


