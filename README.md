# Creating a pipeline to extract tables from PDFs using AWS Step Functions and AWS Textract 

![PDF_table_extraction_pipeline_diagram](https://github.com/codeslp/school_assessments_proj/assets/54224858/38402d63-fa9b-404e-8ce2-c6ca1a77e4c0)

A culinary consulting company has been training school nutrition staff and administrators in the public schools of Oklahoma for several years now. The trainers recorded pre- and post-assessment data and stored it in PDFs and stored multiple years with roughly 12–20 different schools each year. They would like some insights into this data. There are 4 specific tables that they would like to be able to glean insights from that appear in each of these several dozen documents.

I used AWS Textract, which is a machine learning tool that can extract data, while maintaining table structures. I used AWS Step Functions to establish the pipeline flow of the ETL process, Python Lambda functions to do the transformations, S3 as my data lake, and Tableau for visualizations.

## AWS architecture drawing and table ERD: 
https://tinyurl.com/47pau7nu

## Blog posts about this project:
Things I've learned about Step Functions in doing this project: https://medium.com/@brian.farish/aws-step-functions-for-data-pipelines-7fc35e080ad9

Things I've learned about Lambdas in doing this project: https://medium.com/@brian.farish/navigating-aws-lambdas-and-iam-permissions-bd3540451f2d


## Visualizations of derived data in Tableau:
One of the dashboards I made with some of the data from these tables: https://public.tableau.com/app/profile/brian.farish/viz/Cooking-for-Kids-Training-McAlester-2018-2023/CookingforKids-McAlester-2018-23


