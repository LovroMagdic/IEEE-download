import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageTextApp:
    def __init__(self, root, image_paths):
        self.root = root
        self.root.title("Image Viewer with Text Input")
        self.user_text = ""
        self.image_paths = image_paths
        self.current_index = 0

        # Create a label for displaying the image
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Create a text area for input
        self.text_area = tk.Text(root, height=2, width=50)
        self.text_area.pack()
        self.text_area.bind("<Return>", self.on_enter)

        # Display the first image
        self.display_image()

    def display_image(self):
        if self.current_index < len(self.image_paths):
            image_path = self.image_paths[self.current_index]
            try:
                image = Image.open(image_path)
                image = image.resize((800, 300))
                img_display = ImageTk.PhotoImage(image)
                self.image_label.config(image=img_display)
                self.image_label.image = img_display

                # Automatically set focus to the text area
                self.text_area.focus_set()
                self.text_area.delete("1.0", tk.END)  # Clear the text area for new input
            except Exception as e:
                print(f"Error opening image: {e}")
        else:
            print("All images have been displayed.")
            self.root.destroy()

    def on_enter(self, event):
        # Get the text input and print it along with the current image path
        user_text = self.text_area.get("1.0", tk.END).strip()
        user_text = user_text.replace("\n", "")
        image_path = self.image_paths[self.current_index]
        file.write(f"{image_path}|{user_text}\n")
        # print(f"Image Path: {image_path}")
        # print(f"User Input: {user_text}\n")

        # Move to the next image
        self.current_index += 1
        self.display_image()

def check_already_annotated(path):
    already_annotated = []
    csv = open(path, "r")
    for each in csv:
        each = each.replace("\n", "")
        each = each.split("|") # different seperator since , will be in output
        already_annotated.append(each[0])
    csv.close()
    return already_annotated

def reannotation_req(reano_req_list, already_annotated):

    for req in reano_req_list:
        already_annotated.remove(req)

    # not finished, old values still exist in labels.csv file
    return already_annotated

# Main application
image_paths = []

path = "labels.csv"
already_annotated = check_already_annotated(path)

# example of reano req
reano_flag = 0
if reano_flag:
    reano_req_list = ["./CNN/dataset/adversarial attacks in ML.png","./CNN/dataset/adaptive neural controllers.png"]
    already_annotated = reannotation_req(reano_req_list, already_annotated)

file = open("labels.csv", "a")
if "path" not in already_annotated:
    file.write("path|label\n")
path = "./CNN/dataset/"

# to remember already annotated images
images = os.listdir(path)
for image in images:
    full_name = path + image
    if (".png" in image) and (full_name not in already_annotated):
        image_paths.append(full_name)
    elif (".png" in image) and (full_name in already_annotated):
        print(f"{full_name} has been already annotated!")

root = tk.Tk()
app = ImageTextApp(root, image_paths)
root.mainloop()
file.close()