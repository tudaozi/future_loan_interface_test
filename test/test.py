from datetime import datetime

report_name = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
print(report_name)
