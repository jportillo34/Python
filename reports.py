import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


#def generate_report(filename, title, additional_info, table_data):
def generate_report(attachment, title, paragraph):
	styles = getSampleStyleSheet()
	report = SimpleDocTemplate(attachment)
	report_title = Paragraph(title, styles["h1"])

	empty_line = Spacer(1,20)
	data = Paragraph(paragraph)

	#report.build([report_title, empty_line, report_info, empty_line, report_table])
	report.build([report_title, empty_line, data])
