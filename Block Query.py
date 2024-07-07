class Block:
    def __init__(self, name, weight, length, breadth, size, border, shape, colour):
        self.name = name
        self.weight = weight
        self.length = length
        self.breadth = breadth
        self.size = size
        self.border = border
        self.shape = shape
        self.colour = colour

    def query_property(self, property_name):
        # Convert property_name to lowercase for case-insensitive comparison
        property_name = property_name.lower()
        if property_name == "weight":
            return self.weight
        elif property_name == "length":
            return self.length
        elif property_name == "breadth":
            return self.breadth
        elif property_name == "size":
            return self.size
        elif property_name == "border":
            return self.border
        elif property_name == "shape":
            return self.shape
        elif property_name == "colour":
            return self.colour
        else:
            return None  # Property not found

def query_block_properties(block):
    valid_properties = ["weight", "length", "breadth", "size", "border", "shape", "colour"]
    
    while True:
        property_name = input(f"What property do you want to know about {block.name}? ").strip().lower()
        if property_name == "exit":
            break
        elif property_name in valid_properties:
            result = block.query_property(property_name)
            print(f"{property_name.capitalize()}: {result}")
        else:
            print(f"'{property_name}' is not a valid property of {block.name}.")
            print("List of valid properties:")
            print(", ".join(valid_properties))

def main():
    # Create instances of Block for Floor, Wall, Ceiling, Column, and Beam
    floor = Block("Floor", "150kg", "2.5m", "2.5m", "625 sq m", "10m", "Square", "Grey")
    wall = Block("Wall", "100kg", "2.5m", "3m", "75 sq m", "5m", "Rectangle", "White")
    ceiling = Block("Ceiling", "200kg", "5m", "5m", "250 sq m", "15m", "Circle", "Blue")
    column = Block("Column", "300kg", "1m", "1m", "1 sq m", "2m", "Cylinder", "Red")
    beam = Block("Beam", "250kg", "4m", "0.5m", "2 sq m", "3m", "Rectangular", "Green")
    
    blocks = {
        "floor": floor,
        "wall": wall,
        "ceiling": ceiling,
        "column": column,
        "beam": beam
    }

    print("Welcome to Block Properties Query System.")
    print("Available blocks: Floor, Wall, Ceiling, Column, Beam")
    while True:
        block_name = input("Enter the block you want to query properties for (type 'exit' to quit): ").strip().lower()
        if block_name == "exit":
            break
        elif block_name in blocks:
            query_block_properties(blocks[block_name])
        else:
            print(f"'{block_name}' is not a valid block.")
            print("List of valid blocks:")
            print(", ".join(blocks.keys()))

if __name__ == "__main__":
    main()
