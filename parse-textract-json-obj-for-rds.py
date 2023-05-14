



## The structure of this is right but the parsing logic does not exist yet.


from textractcaller.t_call import call_textract, Textract_Features
from trp.trp2 import TDocument, TDocumentSchema
from trp.t_pipeline import order_blocks_by_geo
import trp
import json
import boto3



def lambda_handler(event, context):

    step_state = event['Input']

    # Instantiate the Textract client
    textract = boto3.client('textract')

    # call textract
    analysis_response = textract.get_document_analysis(step_state['tableAnalysisJobId'])
    detection_response = textract.get_document_text_detection(step_state['textDetectionJobId'])


    # -------  FIRST WE WILL PARSE THE TABLES ---------


    # the table analysis doc will be not ordered
    a_doc = TDocumentSchema().load(analysis_response)
    # the ordered_doc has elements ordered by y-coordinate (top to bottom of page)
    ordered_a_doc = order_blocks_by_geo(a_doc)
    # send to trp for further processing logic
    a_trp_doc = trp.Document(TDocumentSchema().dump(ordered_a_doc))

    # Iterate over elements in the document
    for page in a_trp_doc.pages:
        # Print tables
        for table in page.tables:
            for r, row in enumerate(table.rows):
                for c, cell in enumerate(row.cells):
                    # print("Table[{}][{}] = {}-{}".format(r, c, cell.text))




    # -------  THEN WE WILL PARSE THE WORDS AND LINES ---------

    # the table analysis doc will be not ordered
    d_doc = TDocumentSchema().load(detection_response)
    # the ordered_doc has elements ordered by y-coordinate (top to bottom of page)
    ordered_d_doc = order_blocks_by_geo(d_doc)
    # send to trp for further processing logic
    d_trp_doc = trp.Document(TDocumentSchema().dump(ordered_d_doc))


    for page in d_trp_doc.pages:
        # Print lines and words
        for line in page.lines:
           # print("Line: {}--{}".format(line.text))
            for word in line.words:
                # print("Word: {}--{}".format(word.text))