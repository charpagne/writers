import os
from Methods.write_core_ang import AngWriter

ang_dir = "C:\\Users\\SteveJobs\\PycharmProjects\\ang_writer\\Data\\"
ang_in = "test.ang"
ang_out = "test_out.ang"

ang_object = AngWriter((os.path.join(ang_dir, ang_in)), (os.path.join(ang_dir, ang_out)))

