import tkinter as tk
from tkinter import ttk
import requests

class DraggableShapeApp:
    def __init__(self, root):
        """
        Initialize the DraggableShapeApp and enable shape movement on screen

        Args:
            root (tk.Tk): The root window of the application
        """
        # Initialize the window
        self.root = root
        self.root.title("Drag this colorful shape!")

        # Add extra height to make room for dropdown menus
        self.root.geometry("550x650")

        # Initialize the canvas
        self.canvas_width = 550
        self.canvas_height = 550
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()
        self.edge = 50

        # Initialize the dropdown menu for selecting the shape type
        self.shape_type_var = tk.StringVar()
        self.shape_type_var.set('Square')
        self.shape_type_dropdown = ttk.Combobox(root, textvariable=self.shape_type_var,
                                                values=['Square', 'Rectangle', 'Circle', 'Oval', 'Triangle'], state="readonly")
        self.shape_type_dropdown.pack(pady=10)
        self.shape_type_dropdown.bind("<<ComboboxSelected>>", self.reload_shape)

        # Load colors from API
        self.colors = self.get_colors()

        # Initialize the dropdown menu for colors
        self.color_var = tk.StringVar()
        self.color_dropdown = ttk.Combobox(root, textvariable=self.color_var, values=self.colors, state="readonly")
        self.color_dropdown.set('Red to Green')
        self.color_dropdown.pack(pady=10)
        self.color_dropdown.bind("<<ComboboxSelected>>", self.reload_shape)

        # Create the shape to display on the screen, default to Red Square to begin
        self.create_shape()

    def create_shape(self):
        """
        Create and display the selected shape on the canvas
        """
        # Remove the previous shape 
        self.canvas.delete('shape') 
        
        # Get the selected shape type and color sequence
        shape_type = self.shape_type_var.get()
        self.color_sequence = self.color_var.get().lower().split(" to ")
        self.color = self.color_sequence[0]

        # Create the shape on the canvas corresponding to the selected shape type and color
        if shape_type == 'Square':
            self.shape = self.canvas.create_rectangle(280, 280, 320, 320, fill=self.color, tags='shape')
        if shape_type == 'Rectangle':
            self.shape = self.canvas.create_rectangle(270, 280, 330, 320, fill=self.color, tags='shape')
        elif shape_type == 'Circle':
            self.shape = self.canvas.create_oval(280, 280, 320, 320, fill=self.color, tags='shape')
        elif shape_type == 'Oval':
            self.shape = self.canvas.create_oval(270, 280, 330, 320, fill=self.color, tags='shape')
        elif shape_type == 'Triangle':
            self.shape = self.canvas.create_polygon(280, 320, 320, 320, 300, 280, fill=self.color, tags='shape')
        
        # Enable the shape to move on the canvas
        self.bind_shape_events()

    def bind_shape_events(self):
        """
        Bind events to enable the shape to respond to being clicked on and dragged on the screen
        """
        self.canvas.tag_bind('shape', '<ButtonPress-1>', self.on_shape_click)
        self.canvas.tag_bind('shape', '<B1-Motion>', self.on_shape_drag)

    def on_shape_click(self, event):
        """
        Set initial x, y coordinates when the shape is clicked on
        """
        self.start_x = event.x
        self.start_y = event.y
    
    def on_shape_drag(self, event):
        """
        Move the shape based on the existing coordinates and the event of being dragged 
        and change shape color based on position

        Args:
            event (tk.Event): The event triggering the drag
        """
        self.canvas.move(self.shape, event.x - self.start_x, event.y - self.start_y)
        self.start_x = event.x
        self.start_y = event.y

        # Change shape color based on position
        shape_coords = self.canvas.coords(self.shape)
        for coord in shape_coords:
            if coord <= self.edge:
                color = self.color_sequence[1]
                break
            if coord >= self.canvas_width - self.edge:
                color = self.color_sequence[1]
                break
            if coord >= self.canvas_height - self.edge:
                color = self.color_sequence[1]
                break
            else:
                color = self.color_sequence[0]

        self.canvas.itemconfig(self.shape, fill=color)

    def reload_shape(self, event):
        """
        Helper function to recreate the shape when a new color or shape type is selected

        Parameters:
            event (tk.Event): The event triggering the reload
        """
        self.create_shape()

    def get_colors(self):
        """
        Fetch colors from an API or use default colors if the API call fails

        Returns:
            list: List of color sequences to populate the dropdown menu
        """
        api_url = 'http://127.0.0.1:5000/colors'  
        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                return response.json()
            else:
                # Return colors if API call fails
                return ['Red to Green', 'Green to Red', 'Blue to Orange', 'Orange to Blue', 'Purple to Yellow', 'Yellow to Purple']
        except requests.exceptions.RequestException as e:
            # Return colors if API call fails
            print(f"Error fetching colors from API: {e}")
            return ['Red to Green', 'Green to Red', 'Blue to Orange', 'Orange to Blue', 'Purple to Yellow', 'Yellow to Purple']

if __name__ == "__main__":
    root = tk.Tk()
    app = DraggableShapeApp(root)
    root.mainloop()
