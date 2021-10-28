import pandas as pd
from folder_file_name import folder_IngestionReport, file_IngestionReport
from join_files import JoinFail
from init_logger import log

# Logger
logger = log('Ingestion Report')


class IngestionReport:
    def __init__(self, start, finish, env):
        self.start = start
        self.finish = finish
        self.env = env

    def ingestion_report(self):
        ingestion_Report = JoinFail(self.start, self.finish, self.env)
        e2eIngestionReportDetails = ingestion_Report.DetailReport()
        e2eIngestionReportSummary = ingestion_Report.SummaryReport()
        folder_path = folder_IngestionReport(e2eIngestionReportDetails)
        file_name = file_IngestionReport(e2eIngestionReportDetails)
        with pd.ExcelWriter(folder_path + '\\' + file_name) as write:
            e2eIngestionReportDetails[
                ['INGESTION_ID', 'TYPE_OF_MESSAGE', 'CRNT_STATUS', 'INGESTION_SERVICE_MESSAGE_STARTED',
                 'INGESTION_SERVICE_MESSAGE_FINISHED', 'INGESTION SERVICE TOTAL TIME',
                 'MESSAGE_BROKER_STARTED', 'MESSAGE_BROKER_FINISHED', 'MESSAGE BROKER TOTAL TIME',
                 'LCT_ADAPTER_STARTED', 'LCT_ADAPTER_FINISHED', 'LCT ADAPTER TOTAL TIME',
                 'MSG_STATUS', 'COMPUTATION_STARTED', 'COMPUTATION_FINISHED', 'COMPUTATION_STATUS',
                 'COMPUTATION TOTAL TIME',
                 'totalSourcingObjectCount', 'TimeDiff']].to_excel(
                write, index=False, sheet_name='DetailReport')
            e2eIngestionReportDetails[
                ['INGESTION_ID', 'totalCpuTimeMs',
                 'averageCpuTimeMs',
                 'performanceStatus',
                 'totalInvocationCount',
                 'currentInvocationCount',
                 'invocationPerObjectRatio',
                 'totalSourcingObjectCount',
                 'totalProcessedObjectCount'
                 ]].to_excel(
                write, index=False, sheet_name='DetailReportComputation')
            e2eIngestionReportSummary.to_excel(write, index=False, sheet_name='SummaryReport')
            logger.info('INGESTION REPORT CREATED SUCCESSFULLY ! .. path -> ' + folder_path + '\\' + file_name)