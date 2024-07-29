# Data Processing and Anonymization Project

This project includes scripts for generating, parsing, and anonymizing data. It can be run locally or in a Docker container.

## Project Structure

```tree
/data_mask
│
├── generate_data.py # Script to generate CSV data
├── anonymize.py # Script to anonymize CSV data
├── parse.py # Script to parse CSV data according to a template
├── schema.py # Schema definition for the data
├── main.py # Main script to run the full process
├── test.py # Unit tests for the project
├── Dockerfile # Docker configuration file
└── requirements.txt # Python dependencies
```

## File Descriptions

- `generate_data.py`: Generates a CSV file with random data.
- `anonymize.py`: Anonymizes specific columns in the CSV file.
- `parse.py`: Parses the CSV file according to a defined schema.
- `schema.py`: Contains the schema definition and a salt value for hashing.
- `main.py`: Main script that runs the data generation, parsing, and anonymization process.
- `test.py`: Contains unit tests for the project.
- `Dockerfile`: Defines the Docker image and specifies how to build and run the project.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Requirements

- Python 3.9+
- Docker (optional, for running in a container)

## Setup

### Local Setup

1. **Clone the repository**

    ```sh
    git clone <repository-url>
    cd your-project
    ```

2. **Create a virtual environment**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the main script**

    ```sh
    python3 main.py
    ```

5. **Run the tests**

    ```sh
    python3 -m unittest discover -s .
    ```

### Docker Setup

1. **Build the Docker image**

    ```sh
    docker build -t data_mask .
    ```

2. **Run the Docker container**

    ```sh
    docker run -d --name data_mask_container data_mask
    ```

3. **Enter the running container**

    ```sh
    docker exec -it data_mask_container sh
    ```

4. **Check the generated files**

    ```sh
    ls /app
    cat /app/original_data.csv 
    cat /app/anonymized_data.csv 
    ```

5. **Exit the container**

    ```sh
    exit
    ```

5. **Stop the container**

    ```sh
    docker stop data_mask_container
    ```

6. **Remove the container**

    ```sh
    docker rm data_mask_container
    ```

7. **Remove the Docker image (if needed)**

    ```sh
    docker rmi data_mask
    ```
