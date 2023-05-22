import os
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import ImageTk
from time import time
import search
import draw

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Application")
        self.root.geometry("825x500")
        self.root.configure(background="grey")
        
        self.figure = None
        
        # Left side - Image display
        self.image_frame = tk.Frame(self.root, bg="grey")
        self.image_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Right side - Buttons
        self.button_frame = tk.Frame(self.root, bg="grey")
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.create_button = tk.Button(self.button_frame, text="Create Image", command=self.create_image, bg="grey")
        self.create_button.pack(pady=5)
        
        self.download_button = tk.Button(self.button_frame, text="Download Image", command=self.download_image, state=tk.DISABLED, bg="grey")
        self.download_button.pack(pady=5)

        # Bind the window close event to the exit function
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)
        
    def create_image(self):
        parameters = search.search_attractors()
        self.figure = draw.draw(parameters)

        # Save the figure as a temporary image file
        filename = "generated_plot.png"
        self.figure.savefig(filename)

        # Display the generated plot on the left side
        if self.figure:
            # Clear the image frame before displaying the new plot
            for widget in self.image_frame.winfo_children():
                widget.destroy()

            # Load the saved image file
            image = ImageTk.PhotoImage(file=filename)

            # Create a label to display the image
            image_label = tk.Label(self.image_frame, image=image)
            image_label.image = image  # Keep a reference to prevent garbage collection
            image_label.pack()

            # Enable the download button
            self.download_button.config(state=tk.NORMAL)

            # Delete the temporary image file
            os.remove(filename)
        
    def download_image(self):
        # Save the figure as an image file
        filename = str(time()) + ".png"

        # Get the path to the desktop directory
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Save the figure with the desired filename on the desktop
        pathname = os.path.join(desktop_path, filename)
        self.figure.savefig(pathname, dpi=300)
        

        # Display a message box to indicate the successful download
        tk.messagebox.showinfo("Download Complete", "Plot downloaded successfully!")

    def exit_application(self):
        # Handle the window close event
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            if self.figure:
                plt.close(self.figure)  # Close the figure to release resources
            self.root.destroy()
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()