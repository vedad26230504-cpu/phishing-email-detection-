# Count exclamation marks in emails

df['exclamation_count'] = df['email_text'].apply(lambda x: x.count('!'))

# Compare exclamation mark count by email type

df.groupby('email_type')['exclamation_count'].mean()
