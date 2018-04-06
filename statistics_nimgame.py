# pip3 install --user openpyxl


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Analyse:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_comments(self, head_line_number1, head_line_number2):
        with open(self.file_name) as f:
            head_lines = f.readlines()[head_line_number1:head_line_number2]
            head_lines = [line.replace('\n', '') for line in head_lines]
            return head_lines

    def read_data(self, line_number1, line_number2):
        with open(self.file_name) as f:
            temp = f.readlines()[line_number1:line_number2]
            temp = [line.split(' ') for line in temp]
            temp = [line[0:3] for line in temp]
            new_temp = [[round(float(i), 3) for i in inner] for inner in temp]
            new_temp = np.array(new_temp)
            return new_temp

    def analyse_data(self, np_array, raw=45, column=3):
        df = pd.DataFrame(np_array.reshape(raw, column),
                          columns=("Time", "Random Score", "AI Score"))
        data_result = df.describe().loc[['count', 'max', 'min', 'mean', 'std']]
        return data_result


file = Analyse('Time Analysing.txt')
# We used 'wo = without' as a notation to show which features included.
# E.g. cache_wo_ab_classes = Cache and classes have been implemented together without using alpha-beta.

coloumn_head_line = file.read_comments(0, 2)
cache_ab_wo_classes_headline = file.read_comments(2, 3)

cache_ab_wo_classes = file.read_data(3, 48)
analyse_cache_ab_wo_classes = file.analyse_data(cache_ab_wo_classes)

cache_wo_ab_wo_classes = file.read_data(49, 79)
analyse_cache_wo_ab_wo_classes = file.analyse_data(cache_wo_ab_wo_classes, 30, 3)

cache_ab_classes = file.read_data(80, 125)
analyse_cache_ab_classes = file.analyse_data(cache_ab_classes)

cache_wo_ab_classes = file.read_data(181, 196)
analyse_cache_wo_ab_classes = file.analyse_data(cache_wo_ab_classes, 15, 3)

wo_cache_ab_classes = file.read_data(198, 243)
analyse_wo_cache_ab_classes = file.analyse_data(wo_cache_ab_classes)

cache_ab_classes_depth_5 = file.read_data(244, 289)
analyse_cache_ab_classes_depth_5 = file.analyse_data(cache_ab_classes_depth_5)

cache_ab_classes_depth_4 = file.read_data(290, 335)
analyse_cache_ab_classes_depth_4 = file.analyse_data(cache_ab_classes_depth_4)

cache_ab_classes_depth_3 = file.read_data(336, 381)
analyse_cache_ab_classes_depth_3 = file.analyse_data(cache_ab_classes_depth_3)

p = pd.Panel({'d1': analyse_cache_ab_wo_classes,
              'd2': analyse_cache_wo_ab_wo_classes,
              'd3': analyse_cache_ab_classes,
              'd4': analyse_cache_wo_ab_classes,
              'd5': analyse_wo_cache_ab_classes,
              'd6': analyse_cache_ab_classes_depth_3,
              'd7': analyse_cache_ab_classes_depth_4,
              'd8': analyse_cache_ab_classes_depth_5
              })


result_panel = p.to_frame()
print(result_panel)
writer = pd.ExcelWriter("data.xlsx") # export panel to excel file
result_panel.to_excel(writer,"changed")
writer.save()



x1 = list(range(45))
y1 = [i[0] for i in cache_ab_wo_classes]
y2 = [i[0] for i in cache_wo_ab_wo_classes]  # late 30 tests only for (2, 5, 6, 7) and (5, 9, 8, 97)
y3 = [i[0] for i in cache_ab_classes]
y4 = [i[0] for i in cache_wo_ab_classes]  # late 15 tests only for (3, 8, 8, 11, 21)
y5 = [i[0] for i in wo_cache_ab_classes]
y6 = [i[0] for i in cache_ab_classes_depth_3]
y7 = [i[0] for i in cache_ab_classes_depth_4]
y8 = [i[0] for i in cache_ab_classes_depth_5]

f1 = plt.figure(1)
plt.plot(x1, y1, 'g.--', label='Cache + Alpha-Beta without Classes', linewidth=1, markersize=8)
plt.plot(x1, y3, 'r.--', label='Cache + Alpha-Beta + Classes', linewidth=1, markersize=8)
plt.xlabel('Experiment Order')
plt.ylabel('Duration (Second)')
plt.title('Classes-Duration Analysis of Supernim')
plt.legend()
plt.grid(True)
f1.show()

f2 = plt.figure(2)
plt.plot(x1, y6,'g.--',  label='Depth: 3', linewidth=1, markersize=8)
plt.plot(x1, y7,'c.--',  label='Depth: 4', linewidth=1, markersize=8)
plt.plot(x1, y8,'k.--',  label='Depth: 5', linewidth=1, markersize=8)
plt.xlabel('Experiment Order')
plt.ylabel('Duration (Second)')
plt.title('Depth Duration Analysis of Supernim')
plt.legend()
plt.grid(True)
f2.show()

f3 = plt.figure(3)
plt.plot(x1, y5, 'm.--', label='Without Cache + Alpha-Beta + Classes', linewidth=1, markersize=8)
plt.plot(x1, y3, 'r.--', label='Cache + Alpha-Beta + Classes', linewidth=1, markersize=8)
plt.xlabel('Experiment Order')
plt.ylabel('Duration (Second)')
plt.yscale('log', basey=2) # since there was huge gap between two data set, we used log graph.
plt.title('Cache Duration Analysis of Supernim')
plt.legend()
plt.grid(True)
f3.show()

f4 = plt.figure(4)
plt.plot(x1[0:15], y4, 'k.-', label='Cache + Without Alpha-Beta + Classes', linewidth=1, markersize=8)
plt.plot(x1[0:15], y3[15:30], 'r.-',
         label='Cache + Alpha-Beta + Classes', linewidth=1, markersize=8) # we only compare 15 experiment here.
plt.xlabel('Experiment Order')
plt.ylabel('Duration (Second)')
plt.yscale('log', basey=2)
plt.title('Alpha Beta Duration Analysis of Supernim')
plt.legend()
plt.grid(True)
plt.show()

