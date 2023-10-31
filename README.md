
# Reverb Time Calculator

![Project Image](https://i.imgur.com/GKJDZSF.png)

> Calculate the reverb time (T60) in a room based on its materials and dimensions.

## Table of Contents

- [Description](#description)
- [How to Use](#how-to-use)
- [Materials](#materials)
- [Contributing](#contributing)
- [License](#license)

## Description

Welcome to the Reverb Time Calculator! This Python program helps you calculate the reverberation time (T60) in a room. T60 is a measure of how long it takes for sound to decay by 60 decibels after a sound source has stopped.

This calculator takes into account the materials used in the room, their absorption and reflection coefficients, and the room's dimensions. It uses the Sabine formula to estimate the reverb time.

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/ReverbTimeCalculator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ReverbTimeCalculator
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

4. Follow the prompts to select materials for each surface, enter dimensions, and room volume.

5. The program will calculate the reverb time and display the result.

## Materials

The following materials are available for selection, with their absorption, reflection, and density values:

- Concrete: Absorption: 0.03, Reflection: 0.01, Density: 2300
- Brick: Absorption: 0.02, Reflection: 0.03, Density: 1750
- Wood: Absorption: 0.1, Reflection: 0.05, Density: 700
- Glass: Absorption: 0.03, Reflection: 0.1, Density: 2500
- Carpet: Absorption: 0.2, Reflection: 0.05, Density: 200
- Plaster: Absorption: 0.05, Reflection: 0.02, Density: 1200
- Metal: Absorption: 0.01, Reflection: 0.5, Density: 7800
- Curtain: Absorption: 0.3, Reflection: 0.02, Density: 30

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. We welcome any improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

