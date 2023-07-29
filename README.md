
# magik_monkee
magik_monkee is a Python-based tool designed for testing file upload vulnerabilities in web applications. By leveraging a JSON-based database of "magic numbers" or file signatures, magik_monkee identifies and replaces the magic numbers of a selected file extension. This process generates a new file that retains the original content but adopts the magic numbers of the chosen extension. The tool proves invaluable in verifying file upload security, guarding against malicious uploads, and detecting potential bypasses in File Upload functionalities.

## Features
-   Validate and modify magic numbers of uploaded files
-   JSON-based database for storing and managing file signatures
-   Option to list available extensions in the database
-   Ability to get detailed information on selected extensions
-   Easily change the output file extension to a selected one

## Usage
    usage: magik_monkee.py [-h] [-d DATABASE] [-e EXT] [-i] [-l] [-o OUTPUT] [-x] [file_source]

    positional arguments:
      file_source           source file to inject the magic numbers
    
    options:
      -h, --help            			show this help message and exit
      -d DATABASE, --database DATABASE	path to the database to be used
      -e EXT, --ext EXT     			list of extensions to use
      -i, --info            			get detailed information on the selected extensions
      -l, --list            			list all extensions currently available in the database selected
      -o OUTPUT, --output OUTPUT        name of the file to be generated
      -x, --change-extension            change the output extension to the new one selected

## Getting Started
1.  Clone the repository: `git clone https://github.com/MachadoOtto/magik-monkee.git`
2.  Install Python 3 if not already installed.
3.  Prepare your file with the content you want to upload and note its file extension.
4.  Run magik_monkee using the appropriate command-line arguments to modify the magic numbers for the desired file extension.

## Examples
1.  Basic usage to modify magic numbers for a PNG file:

        python magik_monkee.py file_to_upload.png -e png
    
2.  Get detailed information about the PNG extension in the database:

        python magik_monkee.py -i -e png

3.  List all available extensions in the database:

        python magik_monkee.py -l

## Database Manager Submodule
The magik_monkee repository now includes a useful submodule called `db_manager.py` that allows you to manage the JSON-based database used by the tool. This submodule provides the following functionalities:

    usage: db_manager.py [-h] [-a] [-i INFO] [-l] [-n] [-u] [database]
    
    positional arguments:
      database              database file path
    
    options:
      -h, --help            show this help message and exit
      -a, --add             add a new signature to an extension in the database
      -i INFO, --info INFO  get detailed information on the selected extensions
      -l, --list            list all extensions currently available in the database selected
      -n, --new             generate a new empty database file
      -u, --update          update the database file

### Usage
1.  To add a new signature to an extension in the database:
   
        python db_manager.py -a -e <extension> -s <signature> 
    
2.  To get detailed information about an extension in the database:
    
        python db_manager.py -i -e <extension> 
    
3.  To list all available extensions in the database:
    
        python db_manager.py -l 
    
4.  To generate a new empty database file:
    
        python db_manager.py -n 
    
6.  To update the database file with any changes made:

        python db_manager.py -u

## Contributing

Contributions to magik_monkee are welcome! If you find any bugs, have feature requests, or want to improve the tool, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://raw.githubusercontent.com/MachadoOtto/magik-monkee/main/LICENSE) file for details.

## Disclaimer

Use this tool responsibly and only on systems and applications you are authorized to test. The developers are not responsible for any misuse or damage caused by using magik_monkee.

## Contact

For any inquiries or questions, you can reach us at [jorge.machado.ottonelli@gmail.com](mailto:jorge.machado.ottonelli@gmail.com).

_Thank you for using magik_monkee!_
