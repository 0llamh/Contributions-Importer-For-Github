import git
from src import Importer

# reports_repo = git.Repo('C:/Users/pc.smith/PycharmProjects/ngsapps')
# mock_reports_repo = git.Repo("C:/Users/pc.smith/Contributions/NGSReports")
# reports_importer = Importer([reports_repo], mock_reports_repo)
# reports_importer.set_author(['smith.paulcameron@gmail.com', 'pc.smith@ufl.edu'])
# reports_importer.import_repository()


timer_repo = git.Repo('C:/Users/pc.smith/PycharmProjects/self-service')
mock_timer_repo = git.Repo("C:/Users/pc.smith/Contributions/SelfServiceTimer")
timer_importer = Importer([timer_repo], mock_timer_repo)
timer_importer.set_author(['smith.paulcameron@gmail.com', 'pc.smith@ufl.edu'])
timer_importer.set_keep_commit_messages(True)
timer_importer.set_start_from_last(True)
timer_importer.import_repository()


lims_repo = git.Repo('C:/Users/pc.smith/PycharmProjects/lims')
mock_lims_repo = git.Repo("C:/Users/pc.smith/Contributions/myBiotech")
lims_importer = Importer([lims_repo], mock_lims_repo)
lims_importer.set_author(['smith.paulcameron@gmail.com', 'pc.smith@ufl.edu', 'root@icbr-lims-prod.biotech.ufl.edu', 'root@icbr-lims-dev.biotech.ufl.edu'])
lims_importer.set_keep_commit_messages(True)
lims_importer.set_start_from_last(True)
lims_importer.import_repository()
