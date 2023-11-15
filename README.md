# PyPass

A CLI based password manager, buit using the `pycryptodome` library using RSA for key generation and encryption, it also uses `rich` and `inquirer` libraries for user friendly command line interface. 

## Installation

### Windows

1.  Create a virtual environment:  
    ```powershell
    py -m venv venv
    ```
2.  Activate the virtual environment:  
    ```powershell
    venv\Scripts\activate
    ```
3.  Install dependencies from requirements.txt:  
    ```powershell
    pip install -r requirements.txt
    ```

### macOS/linux

1.  Create a virtual environment:  
    ```sh
    python3 -m venv venv
    ```
2.  Activate the virtual environment:  
    ```sh
    source venv/bin/activate
    ```
3.  Install dependencies from requirements.txt:  
    ```sh
    pip install -r requirements.txt
    ```


## Configuration

1. Create a `.env` file in the root of your project.

2. Add the following environment variables to the `.env` file:
   ```python
     PUBLIC_KEY_PATH=path_to_your_public_key_file
     PRIVATE_KEY_PATH=path_to__your_private_key_file
     ROOT_PASSWORD=sha512_hash_of_your_root_password
	 ```

	




