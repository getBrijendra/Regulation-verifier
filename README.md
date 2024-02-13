# Regulation Verifier

This code uses Gen AI for checking if a company website (external communication) follows given regulation guidelines. It provide a simple POST API using Flask framework. Uses OpenAI APIs and Langchain.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

Add your open AI Key
```bash
python .\app.py
```

## Improvement 

Below improvements could be made:

1. As number of token can cross alowed limit for open ai model. So Handle cases with chunked bases.
2. As regulations are not changing frequently. So Using RAG techniques, embedding token can be stored in vector DB. Then based on policy types, find appropriate regulations chunks and find not followed regulation for improvements. 
3. To reduce size of chunks, fire multiple queries based on different techniques like map-reduce etc. depending on use cases.
4. Take steps for verifying the hallucinations.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)