# using this tutorial: https://github.com/aws-samples/aws-ai-intelligent-document-processing/blob/main/02-idp-document-extraction.ipynb

from textractcaller.t_call import call_textract, Textract_Features
from trp import Document
from trp.t_pipeline import order_blocks_by_geo, convert_table_to_list
from textractcaller.t_call import call_textract, Textract_Features, call_textract_expense
from textractprettyprinter.t_pretty_print import convert_table_to_list
import trp
import json
import boto3
import os
import pandas as pd

file = "s3://doc-upload-bucket-doc-parser-app/mcalester-2019-pre-proofconcept.pdf"

resp = call_textract(input_document=file, features=[Textract_Features.TABLES])
tdoc = Document(resp)
dfs = list()

for page in tdoc.pages:
    for table in page.tables:
        tab_list = convert_table_to_list(trp_table=table)
        print(tab_list)
        dfs.append(pd.DataFrame(tab_list))

df1 = dfs[0]
df2 = dfs[1]
df3 = dfs[2]
df4 = dfs[3]
df5 = dfs[4]
df6 = dfs[5]