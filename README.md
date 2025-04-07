# Wannier-Function-Centre-Post-Processing

This repository contains tools to post-process and analyze the Wannier function center, spread, and atomic coordinates extracted from the output files processed by Wannier90.

## Overview

The primary function of this toolset is to calculate the distance between the Wannier function center and the atomic coordinates corresponding to the atoms. The data is processed using a combination of Python and shell scripts. After reading the coordinates of different atoms and the Wannier function center, the distance between the Wannier function center and the atomic coordinate for each atom can be calculated.

## File Structure

- `O_site.dat`: Contains data related to the O-site.
- `README.md`: Documentation for the project.
- `WFC.py`: The Python script that performs the core calculations.
- `atom_wannier_distances.csv`: Stores the calculated distances between the Wannier function center and the atomic coordinates.
- `centre.dat`: Contains the Wannier function center coordinates.
- `centre_site.dat`: Contains data related to the center sites.
- `find_atom_site.sh`: Shell script for identifying the atom site coordinates.
- `find_centre_site.sh`: Shell script for identifying the center site coordinates.
- `LICENSE`: License file for the project.

## Installation

### Prerequisites

- Python 3.x
- Wannier90 (for generating the `.wout` files used in this process)
- Bash shell (for running shell scripts)
- `numpy` and `pandas` Python libraries

### Steps to Install

1. Clone this repository:
    ```bash
    git clone https://github.com/XiaoJiang-Phy/Wannier-Function-Centre-Post-Processing.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Wannier-Function-Centre-Post-Processing
    ```

3. Install the necessary Python packages:
    ```bash
    pip install numpy pandas
    ```

4. Make sure the shell scripts are executable:
    ```bash
    chmod +x find_atom_site.sh find_centre_site.sh
    ```

## Usage

### Step 1: Prepare the input files

Before running the scripts, ensure that the following files are present:
- `prefix.wout`: This file is the output from Wannier90, containing the coordinates of the Wannier functions and atoms.
- `centre.dat` and `centre_site.dat`: These files should contain the center site data and corresponding coordinates.

### Step 2: Run the shell scripts

- To find the atom site coordinates, run:
    ```bash
    ./find_atom_site.sh prefix.wout
    ```
- To find the center site coordinates, run:
    ```bash
    ./find_centre_site.sh prefix.wout
    ```

These scripts will output the necessary data to calculate the distances between the Wannier function center and the atoms.

### Step 3: Run the Python script

Once the necessary files are ready, run the Python script to calculate the distances:

```bash
python WFC.py
