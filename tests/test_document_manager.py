from document_manager import Document, DocumentManager

def test_upload_document():
    manager = DocumentManager()
    document = Document("1", "type1", "2024-01-01", "content1")
    manager.upload_document(document)
    assert document.id in manager.documents
    assert document.id in manager.metadata

def test_search_documents():
    manager = DocumentManager()
    document1 = Document("1", "type1", "2024-01-01", "content1")
    document2 = Document("2", "type1", "2024-01-02", "content2")
    document3 = Document("3", "type2", "2024-01-03", "content3")
    manager.upload_document(document1)
    manager.upload_document(document2)
    manager.upload_document(document3)
    result = manager.search_documents("type1")
    assert len(result) == 2
    assert "1" in result
    assert "2" in result

def test_get_document():
    manager = DocumentManager()
    document = Document("1", "type1", "2024-01-01", "content1")
    manager.upload_document(document)
    result = manager.get_document("1")
    assert result == manager._encrypt_content(document.content)

def test_update_document():
    manager = DocumentManager()
    document = Document("1", "type1", "2024-01-01", "content1")
    manager.upload_document(document)
    new_document = Document("1", "type2", "2024-01-02", "content2")
    manager.update_document("1", new_document)
    assert manager.metadata["1"]["type"] == "type2"

def test_delete_document():
    manager = DocumentManager()
    document = Document("1", "type1", "2024-01-01", "content1")
    manager.upload_document(document)
    manager.delete_document("1")
    assert "1" not in manager.documents
    assert "1" not in manager.metadata

def test_get_non_existent_document():
    manager = DocumentManager()
    try:
        manager.get_document("1")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Document not found"

def test_update_non_existent_document():
    manager = DocumentManager()
    try:
        manager.update_document("1", Document("1", "type1", "2024-01-01", "content1"))
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Document not found"

def test_delete_non_existent_document():
    manager = DocumentManager()
    try:
        manager.delete_document("1")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Document not found"
