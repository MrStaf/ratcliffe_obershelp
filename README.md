# Ratcliffe Obershelp implementation in python

The Ratcliffe Obershelp algorithm is a technique used to measure the similarity between two texts. It was developed by Paul Ratcliffe and Peter Obershelp in the 1970s. The algorithm works by comparing the words used in both texts and calculating a similarity score based on the number of matching words and their respective positions within the texts.

To use the algorithm, the texts are first preprocessed to remove stop words and punctuation. Then, the remaining words are compared and a score is calculated based on their frequency and proximity.

The algorithm is often used in plagiarism detection, document clustering, and information retrieval. It is a popular tool for analyzing large amounts of text data and identifying patterns and similarities between documents.

Overall, the Ratcliffe Obershelp algorithm provides a reliable and effective method for measuring the similarity of two texts. By understanding the principles behind this algorithm, researchers and data analysts can better analyze and interpret text data in a variety of fields.

## Usage

Usage: ratcliff_obershelp.py [options]

Options:
  -h, --help            show this help message and exit
  -f, --file            Compare two files
  -t, --text            Compare two strings, separated by default ';'
  -s SEPARATOR, --separator=SEPARATOR
                        Separator for text comparison
  -v, --verbose

# Demo :

```bash
python .\ratcliff_obershelp.py -f .\textA.txt .\textB.txt
0.9998899647887324
```
