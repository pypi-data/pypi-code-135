import pandas as pd
class FindType:
    def __init__(self, df):
        self.data = df
        self.columns = list(df.columns)

    def _possibles(self):
        return self.data.applymap(lambda x: type(x))

    def _unique_types(self, type_data):
        self.unique_list = []
        for column in self.columns:
            self.unique_list += list(set((type_data[column].values)))
        self.unique_list = list(set(self.unique_list))

    def type_analysis(self, perc=True):
        a = pd.DataFrame(columns=self.columns)
        types = self._possibles()
        self._unique_types(types)
        a['Type'] = self.unique_list
        for i in range(len(self.unique_list)):
            for column in self.columns:
                a.loc[i, column] = (len(types[types[column] == self.unique_list[i]]) / len(types)) * 100
        return a.set_index(['Type'])