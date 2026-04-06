# Count URLs in each email
df['url_count'] = df['email_text'].apply(
    lambda x: len(re.findall(r'http[s]?://\\S+|www\\.\\S+', x))
)

# Compare URL count by email type
df.groupby('email_type')['url_count'].mean()

# Plot URL count by email type
plt.figure(figsize=(8,5))
sns.boxplot(x='email_type', y='url_count', data=df)
plt.title('URL Count by Email Type')
plt.show()
