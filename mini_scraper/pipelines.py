import json
import os

class JsonWriterPipeline:

    def open_spider(self, spider):
        # Construimos la ruta absoluta al archivo data/data.json
        os.makedirs("data", exist_ok=True)
        self.file_path = os.path.join("data", "data.json")
        self.file = open(self.file_path, "w", encoding="utf-8")
        self.file.write("[\n")  # inicio del array JSON
        self.first_item = True

    def close_spider(self, spider):
        self.file.write("\n]")  # cierre del array JSON
        self.file.close()

    def process_item(self, item, spider):
        # Añadimos coma entre items, excepto antes del primero
        if not self.first_item:
            self.file.write(",\n")
        else:
            self.first_item = False

        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line)
        return item
