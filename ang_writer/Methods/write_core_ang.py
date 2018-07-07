import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


class AngWriter:
    def write_header(self, ang_in, ang_out):
        with open(ang_in, 'r') as input_ang, open(ang_out, 'w') as output_ang:
            for line in input_ang:
                if line.startswith("#"):
                    output_ang.write(line)

    def replace_phase(self, segment, ang_in, ang_out):
        seg = plt.imread(segment)
        seg_c = np.concatenate(seg, axis=0)  # convert into a column array
        phase = np.copy(seg_c).astype(int)
        phase[np.where(seg_c == 255)] = 1
        phase[np.where(seg_c < 255)] = 2
        ang = pd.read_csv(ang_in, delim_whitespace=True, comment='#', names={'euler1', 'euler2', 'euler3', 'x',
                                                                         'y', 'iq', 'ci', 'fit', 'phase',
                                                                         'col9', 'col10', 'col11', 'col12',
                                                                         'col13'})
        ang.iloc[ang_in[:, 6] < 0] = 0  # remove any negative confidence index
        ang.iloc[:, 7] = phase
        ang.to_csv(ang_out, index=False, header=False, sep='\t', mode='a', float_format='%.5f')


class Phase:
    def __init__(self, number):
        self.number = number
        self.materialName = ''
        self.formula = ''
        self.info = ''
        self.symmetry = 0
        self.latticeConstants = [0] * 6  # 3 constants & 3 angles
        self.numberFamilies = []
        self.hklFamilies = []
        self.elasticConstants = []
        self.categories = []


class PhaseHeader:
    def _init_(self, filename_in, filename_out):  # read and store info about input .ang file
        with open(filename_in) as file_in:
            for line in file_in:
                if line.startswith("#"):
                    tokens = re.split('\s+', line.strip())
                    if tokens[1] == 'Phase':
                        self.phaseId = float(tokens[2])
                    elif tokens[1] == 'MaterialName':
                        self.materialName = str(tokens[2])
                    elif tokens[1] == 'Formula':
                        self.formula = str(tokens[2])
                    # on s'en tape de 'Info', jamais rempli
                    elif tokens[1] == 'Symmetry':
                        self.symmetry = int(tokens[2])
                    elif tokens[1] == 'LatticeConstants':
                        values = [0] * 6
                        values[0] = float(tokens[2])
                        values[1] = float(tokens[3])
                        values[2] = float(tokens[4])
                        values[3] = float(tokens[5])
                        values[4] = float(tokens[6])
                        values[5] = float(tokens[7])
            # Code shit with phase properties using class phase

            with open(filename_out) as file_out:
                file_out.write()