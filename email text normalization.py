# Count exclamation marks in emails
df['exclamation_count'] = df['email_text'].apply(lambda x: x.count('!'))

# Compare exclamation mark count by email type
df.groupby('email_type')['exclamation_count'].mean()

# Plot exclamation mark count by email type
plt.figure(figsize=(8,5))
sns.boxplot(x='email_type', y='exclamation_count', data=df)
plt.title('Exclamation Mark Count by Email Type')
plt.savefig('outputs/exclamation_count_analysis.png')
plt.show()

# Count uppercase words in emails
df['uppercase_word_count'] = df['email_text'].apply(
    lambda x: sum(word.isupper() for word in x.split())
)

# Compare uppercase word count by email type
df.groupby('email_type')['uppercase_word_count'].mean()

# Plot uppercase word count by email type
plt.figure(figsize=(8,5))
sns.boxplot(x='email_type', y='uppercase_word_count', data=df)
plt.title('Uppercase Word Count by Email Type')
plt.savefig('outputs/uppercase_word_analysis.png')
plt.show()
