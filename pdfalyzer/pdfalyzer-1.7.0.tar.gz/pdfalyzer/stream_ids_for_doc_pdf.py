stream_ids = [426, 424, 4, 411, 412, 416, 419, 421, 423]

for id in stream_ids:
    node = pdfalyzer.find_node_by_idnum(id)
    stream_data = node.obj.get_data()
    print(f"ID: {id}, length of stream: {len(stream_data)}")
