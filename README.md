# Transformer-based News Search Engine

This is a Transformer-based News Search Engine built with Streamlit, SentenceTransformer, and Faiss.

The search engine allows users to enter search queries and retrieves relevant news articles based on semantic similarity. It utilizes a pre-trained transformer model (BERT-based) for encoding text into dense vectors and Faiss for efficient similarity search.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ArchitJambhule1011/Transformer_based_search_tool.git

2. Install the required dependencies:

    ```pip install -r requirements.txt```

3. Run the application:

    ```streamlit run app.py```

4. Due to the large nature of some files they are stored in Google drive, these include the Preprocessed_data.csv file and the faiss_index.pickle file

     ```https://drive.google.com/drive/folders/1kDJMznqA5sXjDIepxBdugdav3bAMayPX?usp=sharing```

Download the files and place the faiss_index.pickle file in the models folder, and the data file into the Data folder

## Usage

1. Open the application in your web browser (http://localhost:8501).

2. Enter your search query in the search box.

3. Press Ctrl + Enter to seach for the query.

4. The search engine will retrieve relevant news articles based on your query and display them in the result section

## License

This project is licensed under the MIT License