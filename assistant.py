import json
import os
import threading

class Assistant:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.lock = threading.Lock()
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filename):
            self._save_notes([])
        else:
            try:
                self._load_notes()
            except json.JSONDecodeError:
                self._save_notes([])

    def _load_notes(self):
        with self.lock:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)

    def _save_notes(self, notes):
        with self.lock:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(notes, f, ensure_ascii=False, indent=2)

    def add_note(self, note):
        notes = self._load_notes()
        notes.append(note)
        self._save_notes(notes)

    def list_notes(self):
        return self._load_notes()

    def search_notes(self, keyword):
        notes = self._load_notes()
        return [n for n in notes if keyword.lower() in n.lower()]
