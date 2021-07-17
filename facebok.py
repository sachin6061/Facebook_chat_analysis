import json
# import emoji
import pandas as pd
file_path = "message.json"
with open(file_path) as file:
    chat_hist = json.load(file)
print(chat_hist.keys())
# authors = chat_hist['participants']
df = pd.DataFrame(chat_hist['messages'])
df["Date"] = pd.to_datetime(df["timestamp_ms"])
print('Chat members', df.sender_name.unique())
print('Total chat members', len(df.sender_name.unique()))

# df = df.dropna()
# print(df.content.Unique())
# df["emoji"] = df["Message"].apply(split_count)

print(df.keys())
frnds = df.sender_name.unique()
frnds_author = []
message_count = []

for i in range(len(frnds)):
        # Filtering out messages of particular user
    req_df = df[df["sender_name"] == frnds[i]]
    frnds_author.append(frnds[i])
    message_count.append(req_df.shape[0])

print('Most active user in chat')
data_df = pd.DataFrame({'author': frnds_author, 'message_count': message_count})
print(data_df.max())
