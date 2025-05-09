# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class ReportConfig:

    # Camel casing is used for the member variables as they are going to be serialized and camel case is standard for JSON keys

    reportId = None
    reportName = None
    embedUrl = None
    datasetId = None
    userName = None
    rlsRole = None


    def __init__(self, report_id, report_name, embed_url, dataset_id = None, user_name = None, rlsRole = None):
        self.reportId = report_id
        self.reportName = report_name
        self.embedUrl = embed_url
        self.datasetId = dataset_id
        self.userName = user_name
        self.rlsRole = rlsRole