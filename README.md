# PyScrape

A CLI based password manager, buit using the `pycryptodome` library using RSA for key generation and encryption, it also uses rich and inquirer library for user friendly command line interface. 

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

### macOS

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

### Linux

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
 	 BREVO_API_KEY=your_brevo_api_key
     JSON_FILE_PATH=path_to_json_file
     USER_AGENT=your_browser_user_agent
     SENDER=senders_email
     RECEIVER_NAMES=names_of_receivers # seperated by comma if more than 1
     RECEIVER_EMAILS=emails_of_receivers # seperated by comma if more than 1
	 ```

	




