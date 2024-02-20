import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, database) -> None:
        self.conn = sqlite3.connect(database + ".db")
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, 
                    title TEXT, 
                    content TEXT NOT NULL );''')
    
    def add(self, nota: Note):
        self.conn.execute('''INSERT INTO note (id, title, content) 
                VALUES (?, ?, ?)''', (nota.id, nota.title, nota.content))
        self.conn.commit()
    
    def get_all(self):
        notes = []
        cursor = self.conn.execute('''SELECT id, title, content FROM note''')
        for linha in cursor:
            ident = linha[0]
            titulo = linha[1]
            cont = linha[2]
            notes.append(Note(id=ident, title=titulo, content=cont))
        return notes
    
    def update(self, entry: Note):
        self.conn.execute('''UPDATE note SET title = ?, content = ? WHERE id = ?''', (entry.title, entry.content, entry.id))
        self.conn.commit()
    
    def delete(self, note_id):
        self.conn.execute('''DELETE FROM note WHERE id = ?''', (note_id,))
        self.conn.commit()