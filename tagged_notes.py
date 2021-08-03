from datetime import datetime

class Note:
    def __init__(self, time, tags, content):
        self.time = time
        self.tags = tags
        self.content = content

    def __repr__(self):
        return f"Time: {self.time}\n------------\n{self.content}\n\nTags: {self.tags}"

def main():
    today = str(datetime.now().strftime("%d-%m-%Y"))
    file_name = f"/home/sarthak/Notes/note-{today}.md"
    notes = []
    
    with open(file_name, "r") as file:
        notes = ( file.read().strip().split("\n\n")[1:] )
        file.close()
    
    notes = [i.split("\n") for i in notes]
    notes_dict = {}
    
    for element in notes:
        time = element[0][3:]
        tags = element[1][2:-2].strip().split(",")
        content = element[2]
    
        note = Note(time, tags, content)
        notes_dict[note.time] = note
    
    file = open(f"{today}-final.txt", "w")
    for i in notes_dict.keys():
        file.write(str(notes_dict[i]))
        file.write("\n\n\n")
    file.close()

if __name__ == "__main__":
    main()
