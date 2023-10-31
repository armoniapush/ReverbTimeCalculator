import pdb


def calculate_reverb_time(materials, room_volume):
    try:
        total_absorption = 0
        total_reflection = 0
        total_density = 0

        num_surfaces = int(input("Enter the number of surfaces: "))
        surfaces = []

        for i in range(num_surfaces):
            print(f"Select a material for Surface {chr(65+i)}:")
            material_options = "\n".join([f"{j} - {material}" for j, material in enumerate(materials.keys(), 1)])
            print(material_options)
            
            while True:
                try:
                    material_option = int(input(f"Enter the number for Surface {chr(65+i)}: "))
                    if 1 <= material_option <= len(materials):
                        break
                    else:
                        print("Invalid material option. Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            material = list(materials.keys())[material_option - 1]
            surfaces.append(material)

        for i, surface in enumerate(surfaces):
            print(f"Enter the dimensions for Surface {chr(65+i)}:")
            length = float(input(f"Length: "))
            width = float(input(f"Width: "))
            height = float(input(f"Height: "))

            surface_volume = length * width * height
            surface_area = 2 * (length * width + length * height + width * height)

            total_absorption += materials[surface]["absorption"] * surface_area
            total_reflection += materials[surface]["reflection"] * surface_area
            total_density += materials[surface]["density"] * surface_volume

        # Use the Sabine formula for T60
        T60 = 0.161 * (room_volume / total_absorption)

        return T60
    except ValueError:
        print("Invalid input. Please enter numeric values for dimensions.")
        return None


if __name__ == "__main__":
    materials = {
        "concrete": {"absorption": 0.03, "reflection": 0.01, "density": 2300},
        "brick": {"absorption": 0.02, "reflection": 0.03, "density": 1750},
        "wood": {"absorption": 0.1, "reflection": 0.05, "density": 700},
        "glass": {"absorption": 0.03, "reflection": 0.1, "density": 2500},
        "carpet": {"absorption": 0.2, "reflection": 0.05, "density": 200},
        "plaster": {"absorption": 0.05, "reflection": 0.02, "density": 1200},
        "metal": {"absorption": 0.01, "reflection": 0.5, "density": 7800},
        "curtain": {"absorption": 0.3, "reflection": 0.02, "density": 30},
    }

    print("Welcome to the Reverb Time Calculator!")
    room_volume = float(input("Enter room volume (cubic meters): "))

    reverb_time = calculate_reverb_time(materials, room_volume)

    if reverb_time is not None:
        print(f"The estimated reverb time for the room is {reverb_time:.5f} seconds.")
