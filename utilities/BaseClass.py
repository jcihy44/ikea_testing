from prettytable import PrettyTable

from utilities.logger import LogGen


def dict_to_table(dictionary):
    headers = [k for k, v in dictionary.items() if v not in ["N/A", None]]
    t = PrettyTable(headers)
    t.add_row([v for k, v in dictionary.items() if v not in ["N/A", None]])
    return str(t)


class BaseClass:
    logger = LogGen.loggen()