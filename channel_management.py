import pickle

def init_channel_list() :
    channel_list = []
    with open("channels", 'wb') as file :
        pickle.dump(channel_list, file)

def add_a_channel(channel_id) :
    with open("channels", 'rb') as f1 :
        channel_list = pickle.load(f1)
    channel_list.append(channel_id)
    with open("channels", 'wb') as f2 :
        pickle.dump(channel_list, f2)

def get_channels_list() :
    with open("channels", 'rb') as file :
        channel_list = pickle.load(file)
    return channel_list