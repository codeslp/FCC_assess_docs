from textractcaller.t_call import call_textract, Textract_Features
from trp.trp2 import TDocument, TDocumentSchema
from trp.t_pipeline import order_blocks_by_geo
import trp
import json
import boto3
import os

# call textract:
j = call_textract(input_document='s3://doc-upload-bucket-doc-parser-app/mcalester-2019-pre-proofconcept.pdf')

# the t_doc will be not ordered
t_doc = TDocumentSchema().load(j)
# the ordered_doc has elements ordered by y-coordinate (top to bottom of page)
ordered_doc = order_blocks_by_geo(t_doc)
# send to trp for further processing logic
trp_doc = trp.Document(TDocumentSchema().dump(ordered_doc))

# Open a file for writing
with open('txt-obj-temp.txt', 'w') as f:
    # Iterate over elements in the document
    for page in trp_doc.pages:

        # Print lines
        for line in page.lines:
            f.write("Line: {}\n".format(line.text))

        # Print tables
        for table in page.tables:
            for r, row in enumerate(table.rows):
                for c, cell in enumerate(row.cells):
                    f.write("Table[{}][{}] = {}-{}\n".format(r, c, cell.text))
