    # explicit definition of pyarrow.lib.Table

        table = pa.table({
            "n_legs": [ 2, 2, 4, 4, 5, 100 ],
            "animal": ["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"],
        })
        ic(table)

        df = pd.read_csv("dat/tiny.csv")
        ic(df)


    # show metadata for pyarrow.lib.Table

        for i in range(pq_file.num_row_groups):
            row_group: pyarrow.lib.Table = pq_file.read_row_group(i)  # pylint: disable=I1101
            ic(row_group)

            columns = row_group.column_names
            ic(columns)

            for col, col_name in enumerate(columns):
                ic(pq_file.schema.column(col))
                ic(col_name, row_group.column(col))
