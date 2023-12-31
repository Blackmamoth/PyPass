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
3. You can also save these in your system's environment variable directly. 

4. To generate and save your public and private keys run the `generate_keys.py` file inside `prerun` directory, and use that file path in the env variables above.

5. Also, to generate the hash for your root password run the `hash_root_password.py` file inside `prerun` directory, and use them in the env variable above.

## Structure

1. Following should be the structure of the file, when importing passwords:

    ```json
        [
              {
                  "application": "name_of_the_application",
                  "password": "unencrypted_password"
              }
        ]
    ```

2. Keep a note that, password in this json file should not be encrypted. The password will be automatically encrypted, while the importing process


	




