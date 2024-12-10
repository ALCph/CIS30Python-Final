#1.)
# The rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # The sets
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    # The gets
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    # Calculations
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height
    
# A function to print the outputs
    def display(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")

# The example function call from the document
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    rect.display()
#--------------------------------------------------------

#2.)
def count_frequencies(list):
    # An empty dictionary used for counting
    frequency_dict = {}
    # the For loop to go through the input string and adjusting the count
    for word in list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

# The example usage from the document to test the code
input_strings = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency_count = count_frequencies(input_strings)
print("Frequency Count:", frequency_count)

