# Draggable Shape App

This code is a solution to the given Challenge #1:
> Create an interface in Python to display a draggable shape in the middle of the screen.  
The shape should change color as it moves from the center to the edge of the screen.  
Allow user to choose the type of shape and a sequence of changing colors from a dropdown list.  
The list should be populated on page load via API call to a service written in Python.  

## Usage

1. Clone the repository and navigate to the project's directory.

2. Create a virtual environment using `pipenv` using the provided `Pipfile`.
~~~
pipenv install
~~~

3. Ensure you have Python 3.9, `tkinter`, `flask`, and `requests` installed in your virtual environment.

4. Ensure there is nothing running on `127.0.0.1:5000`.

5. Run the colors API in a separate terminal:
~~~
pipenv run python colors_api.py
~~~

6. Run the program in a separate terminal using 
~~~
pipenv run python main.py
~~~

7. Utilize the dropdown menus to select a color sequence and shape. 

8. Move the shape towards the edge of the screen to see the shape change colors. 
