import unittest
from document import Document, RedditDocument, ArxivDocument, Preprocessing
from author import Author
from corpus import Corpus

class TestDocument(unittest.TestCase):
    def test_document_creation(self):
        doc = Document("titre", "2024-01-01", "http://site.com", "This is a test document.")
        self.assertEqual(doc.titre, "titre")
        self.assertEqual(doc.date, "2024-01-01")
        self.assertEqual(doc.url, "http://site.com")
        self.assertEqual(doc.texte, "This is a test document.")

class TestAuthor(unittest.TestCase):
    def test_author_creation(self):
        author = Author("Guillaume Panighetti", 0)
        self.assertEqual(author.name, "Guillaume Panighetti")
        self.assertEqual(author.ndoc, 0)

    def test_author_add_doc(self):
        author = Author("Guillaume Panighetti", 0)
        doc = Document("Titre", "2024-01-01", "http://site.com", "Text")
        author.addDoc(doc, 1)
        self.assertEqual(len(author.production), 1)

class TestCorpus(unittest.TestCase):
    def setUp(self):
        doc1 = Document("Titre1", "2024-01-01", "http://site.com/1", "Text1")
        doc2 = Document("Titre2", "2024-01-02", "http://site.com/2", "Text2")
        author1 = Author("Guillaume Panighetti", 0)
        author1.addDoc(doc1, 1)
        author1.addDoc(doc2, 2)
        id2doc = {1: doc1, 2: doc2}
        authors = {"Guillaume Panighetti": author1}
        self.corpus = Corpus("Test Corpus", authors, id2doc)

    def test_corpus_creation(self):
        self.assertEqual(self.corpus.name, "Test Corpus")
        self.assertEqual(len(self.corpus.authors), 1)
        self.assertEqual(self.corpus.ndoc, 2)
        self.assertEqual(self.corpus.naut, 1)

    def test_corpus_get_docs(self):
        docs = self.corpus.getDocs()
        self.assertEqual(len(docs), 2)
        self.assertEqual(docs[0].titre, "Titre1")  # Le premier document est le plus récent, donc le titre devrait être "Title1"
        self.assertEqual(docs[1].titre, "Titre2")  # Le deuxième document est le plus ancien, donc le titre devrait être "Title2"

if __name__ == '__main__':
    unittest.main()
