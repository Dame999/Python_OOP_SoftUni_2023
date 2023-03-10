from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        try:
            category = [c for c in self.categories if c.id == category_id][0]
            category.edit(new_name)
        except IndexError:
            pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        try:
            topic = [t for t in self.topics if t.id == topic_id][0]
            topic.edit(new_topic, new_storage_folder)
        except IndexError:
            pass

    def edit_document(self, document_id: int, new_file_name: str):
        try:
            document = [d for d in self.documents if d.id == document_id][0]
            document.edit(new_file_name)
        except IndexError:
            pass

    def delete_category(self, category_id: int):
        try:
            category = [c for c in self.categories if c.id == category_id][0]
            self.categories.remove(category)
        except IndexError:
            pass

    def delete_topic(self, topic_id):
        try:
            topic = [t for t in self.topics if t.id == topic_id][0]
            self.topics.remove(topic)
        except IndexError:
            pass

    def delete_document(self, document_id):
        try:
            document = [d for d in self.documents if d.id == document_id][0]
            self.documents.remove(document)
        except IndexError:
            pass

    def get_document(self, document_id):
        try:
            document = [d for d in self.documents if d.id == document_id][0]
            return document
        except IndexError:
            pass

    def __repr__(self):
        documents = []
        for d in self.documents:
            documents.append(str(d))
            
        return '\n'.join(documents)