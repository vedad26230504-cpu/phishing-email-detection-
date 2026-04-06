# List of suspicious phishing words

suspicious_words = ['urgent', 'verify', 'password', 'account', 'bank', 'click', 'login', 'limited', 'suspended']

# Count suspicious words in each email

df['suspicious_word_count'] = df['email_text'].apply(
    lambda x: sum(word in x.lower() for word in suspicious_words)
)

# Compare suspicious word count by email type

df.groupby('email_type')['suspicious_word_count'].mean()
