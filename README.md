# udacity-nd-python-meme-generator
Udacity Nano Degree: Motivational Meme Generator

# Basic Instructions

In order to run the applications, please follow the below setup steps:

- Step 1: Under the root folder. Create & activate a new virtual environment 
    ```bash
    $ python3.11 -m venv venv
    $ source ./venv/bin/activate
    # When all tests are completed, we can deactivate the current virtual environment
    $ deactivate
    ```
- Step 2: Install dependencies in the "requirements.txt"
    ```bash
    $ pip install -r requirements.txt
    ```
- Step 3: Install xpdf CLI.
    ```bash
    $ sudo apt-get install -y xpdf
    ```

Under the "***src***" folder, we run the below commands:

Meme generator's CLI tests:

```bash
$ cd src
$ python3 meme.py   # returns ./tmp/meme_xander_1.jpg
$ python3 meme.py --path "../image_tests/istockphoto-1457952279-1024x1024.jpg" # returns ./tmp/meme_istockphoto-1482199015-1024x1024.jpg
$ python3 meme.py --path "../image_tests/istockphoto-1457952279-1024x1024.jpg" --body 'this is my meme' --author 'tumo' # returns ./tmp/meme_istockphoto-1457952279-1024x1024.jpg
```

Flask app's tests:
```bash
$ python3 app.py
# Press "Random" or "Creator"
# If press "Creator" plz use the below URL:
# https://plus.unsplash.com/premium_photo-1668606763482-8dd2042c934e?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
```
# Brief Descriptions of Modules

1. MemeEngine: inside src folder
   - Role & Responsibility: Load image, resize image & insert a quote with author then save the processed image to the local disk.
   - Dependencies: PIL
   - How to use?
     - Create an MemeEngine instance with desired folder containing processed image: ```meme = MemeEngine('./tmp')```
     - Create the meme with given path to the input image, text & author ```path = meme.make_meme(img, quote.body, quote.author)```

2. QuoteEngine: inside src folder
   - Role & Responsilibity: Parse quotes from various input file formats: PDF, CSV, Docx, Txt and returns a list of QuoteModel encapsulating body text & author
   - Dependencies: xpdf which is called by subprocess to convert pdf to text; docx to process docx file; pandas to process CSV
   - How to use?
     - We implemented an encapsulating class which is Ingestor, only need to pass a given file path to ```Ingestor.parse(f)``` it will select the proper module based on the file extension.

3. image_tests contains a free test image

# Project Rubric

## I. Project Setup and Code Style

1. Write code that is PEP compliant and follows common programming best practices.

    The code adheres to the PEP 8 style guide and follows common best practices, including:

   - Variable and function names are clear.
   - The code is DRY (Don’t Repeat Yourself) and methods demonstrate the principle of composition.


2. Create basic documentation.

    All included docstrings and comments adhere to PEP 8 standards. 
    A README file is included in the project root and includes:

    - an overview of the project.
    - instructions for setting up and running the program.
    - a brief description of the roles-and-responsibilities of all sub-modules including dependencies and examples of how to use the module.

3. Consume public libraries using virtual environments.

    The code makes use of public libraries using a virtual environment with the bash command
    ```bash
        $ python3.11 -m venv ./venv
    ```

    All required dependencies are listed in the root requirements.txt file which was created using the bash command.
    ```bash
        $ pip freeze > requirements.txt
    ```

    The program runs with no errors.

    (Optional) If git is used, the virtual environment directory is added to the .gitignore file.

4. Implement basic Python exception handling.

    If the program encounters a common error case (e.g. attempting to load an incompatible filetype), it throws an exception.

    All exceptions include a human-readable message.

    (Optional) Make your exception handling even more awesome:

    Define custom exception classes for different types of exceptions—for things like *Invalid File, Invalid Text Input (e.g. too long)
    Use os.walk to automatically discover ingestible files in a directory

5. Create Python modules.

	
    Classes are organized into multiple directories, with related classes being placed together.

    Each module directory includes a proper __init__.py file.


## II. Quote Engine Module

1. Implement basic object-oriented data structures.

	
    - The code includes a Python class that defines a QuoteMode object, which contains text fields for body and author. The class overrides the correct methods to instantiate the class and print the model contents as: ”body text” - author

    - All related classes are defined in a directory that includes valid __init__.py files to declare the package.

2. Identify when to use Abstract Base Classes (ABC) in Python and implement this design pattern in the code.

    The project contains an abstract base class, IngestorInterface, which defines:

    - A complete classmethod method to verify if the file type is compatible with the ingestor class.

    - An abstract method for parsing the file content (i.e., splitting each row) and outputting it to a Quote object.

    - Only non-abstract classes should be complete.

    > Hint: Classmethods can access class variables, which can be redefined by children classes.

3. Ingest text files using the native file library.

    The project contains a **TextIngestor** class.

    The class inherits the **IngestorInterface**.

    The class does not depend on any 3rd party library to complete the defined, abstract method signatures to parse Text files.

    The parse method returns a valid **QuoteModel**

4. Ingest DOCX files using the python-docx library.

    The project contains a DocxIngestor class.

    The class inherits from the IngestorInterface class.

    The class depends on the python-docx library to complete the defined, abstract method signatures to parse DOCX files.

    The parse method returns a valid QuoteModel

5. Ingest PDF files using CLI tools.

    The project contains a PDFIngestor class.

    The PDFIngestor class inherits from the IngestorInterface class.

    The PDFIngestor class utilizes the subprocess module to call the pdftotext CLI utility—creating a pipeline that converts PDFs to text and then ingests the text.

    The class handles deleting temporary files.

    The parse method returns a valid QuoteModel

    > NOTE: Do not use the pdftotext PIP Library - we'd like you to demonstrate your understanding of the subprocess module.

6. Ingest CSV files using the pandas library.

    The project contains a CSVIngestor class.

    The class inherits the IngestorInterface.

    The class depends on the pandas library to complete the defined, abstract method signatures to parse CSV files.

    The parse method returns a valid QuoteModel

7. Implement class inheritance in Python using the strategy object design pattern and apply DRY (don't repeat yourself) principles

    The DocxIngestor, PDFIngestor, CSVIngestor, and TextIngestor classes should realize the IngestorInterface abstract base class.

    Methods that have shared responsibilities are fully defined in the parent class.

    Excess code is not repeated across the classes.

    All ingestors are packaged into a main Ingestor class. This class encapsulates all the ingestors to provide one interface to load any supported file type.

## III. Meme Generator Module

1. Use the Pillow library to perform basic image operations.

    The project defines a MemeGenerator module with the following responsibilities:

    Loading of a file from disk
    Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
    Add a caption to an image (string input) with a body and author to a random location on the image.
    The class depends on the Pillow library to complete the defined, incomplete method signatures so that they work with JPEG/PNG files.

    The method signature to make the meme should be: make_meme(self, img_path, text, author, width=500) -> str #generated image path

    The init method should take a required argument for where to save the generated images: __init__(self, output_dir...).



## IV. Package your Application

1. Use Python arg variables for CLI execution.

    The project contains a main.py file that uses the ImageCaptioner, DocxIngestor, PDFIngestor, and CSVIngestor methods to generate a random captioned image.

    The program must be executable from the command line.

    The program takes three OPTIONAL arguments:

    A string quote body
    A string quote author
    An image path
    The program returns a path to a generated image.
    If any argument is not defined, a random selection is used.


2. Interface with web resources using flask and requests.

    The project completes the Flask app starter code in app.py. All @TODO tasks listed in the file have been completed.

    app.py uses the Quote Engine module and Meme Generator modules to generate a random captioned image.

    app.py uses the requests package to fetch an image from a user submitted URL.

    The flask server runs with no errors
