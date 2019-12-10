def discriminate_data(labeled_data):
     
     relevant = list()
     irrelevant = list()
     maybe = list()
     
     
     for data in labeled_data['examples']:
         metadata = dict()
         if data['classifications'][0]['classname'] == 'Relevant':
             metadata = data['metadata']
             metadata['post'] = data['content']
             relevant.append(metadata)
         
         elif data['classifications'][0]['classname'] == 'Irrelevant':
             metadata = data['metadata']
             metadata['post'] = data['content']
             irrelevant.append(metadata)
             
         else:
             metadata = data['metadata']
             metadata['post'] = data['content']
             maybe.append(metadata)
     data_dict = dict()
     data_dict['relevant'] = relevant
     data_dict['irrelevant'] = irrelevant
     data_dict['maybe'] = maybe
     return data_dict
             