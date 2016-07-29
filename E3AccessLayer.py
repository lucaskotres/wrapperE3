import win32com.client


class e3comm(object):

    def __init__(self):

        self.eComCall = win32com.client.Dispatch("E3DataAccess.E3DataAccessManager.1")