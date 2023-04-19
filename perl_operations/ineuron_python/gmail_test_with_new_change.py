"""
Email Module
"""

__copyright__ = "Copyright (C) 2022, Intel Corporation"
__license__ = "All Rights Reserved"

# standard library

import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate

# local library

# from utils import common
# from utils import intel

EMAIL_FROM ='prashanthx.adaveni@intel.com'

EMAIL_TO = ['prashanthx.adaveni@intel.com']

FAULT_TEMPLATE = """
Tool    : {tool}
Command : {command}
Start   : {start}
End     : {end}
================================================================================
Machine:
    Hostname : {hostname}
    System   : {system}
================================================================================
Environment:
================================================================================
Exception:
================================================================================
Traceback:
"""

def email_fail(opts, **kwargs):
    """Send email if tool failed"""

    # Compose message

    system = intel.sysname_ct()
    tool_name = kwargs['tool_name']

    mailargs = {
        'tool': tool_name,
        'start': time.ctime(kwargs['start_time']),
        'end': time.ctime(kwargs['end_time']),
        'system': system,
        'command': opts.cmd,
        'hostname': os.uname()[1],
    }

    txt = MIMEMultipart()
    txt['Subject'] = f"{tool_name} {opts.cmd} - {'prashanth'}"
    txt['From'] = EMAIL_FROM
    txt['To'] = ", ".join(EMAIL_TO)
    txt['Date'] = formatdate(localtime=True)
    txt.attach(MIMEText(FAULT_TEMPLATE.format(**mailargs)))

    # # attach log file
    #
    # with open(kwargs['logfile'], "rb") as infile:
    #     part = MIMEApplication(infile.read(), Name=kwargs['logfile'])
    #     attachment = f"attachment; filename={os.path.basename(kwargs['logfile'])}"
    #     part['Content-Disposition'] = attachment
    #     txt.attach(part)

    # send mail

    common.sendmail(msg=txt, From=EMAIL_FROM, To=EMAIL_TO)