class ImportedSummary:
    def __init__(self):
        self.succeeded_count = 0
        self.failed_count = 0

class  ImportingUserGroup:

    def __init__(self):
        self.duplicated = []
        self.banned = []
        self.normal = []


def import_users_from_file(fp):
        importing_user_group = ImportingUserGroup()
        for line in fp:
            parsered_user = parse_user(line)
