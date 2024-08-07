from langchain_community.document_loaders import DirectoryLoader


def load_documents(BASE_DIR):
    data_dir = BASE_DIR / "data"
    loader = DirectoryLoader(data_dir)
    documents = loader.load()
    len(documents)


