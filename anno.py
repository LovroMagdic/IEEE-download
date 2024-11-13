import tkinter as tk
from PIL import Image, ImageTk
import os

file = open("lables.csv", "w")
file.write("path,label\n")

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
                image = image.resize((1000, 400))
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
        image_path = self.image_paths[self.current_index]
        file.write(f"{image_path},{user_text}\n")
        # print(f"Image Path: {image_path}")
        # print(f"User Input: {user_text}\n")

        # Move to the next image
        self.current_index += 1
        self.display_image()

# Main application
image_paths = []

path = "./CNN/dataset/"

images = os.listdir(path)
for image in images:
    if ".png" in image:
        image_paths.append(path + image)
root = tk.Tk()
app = ImageTextApp(root, image_paths)
root.mainloop()
file.close()