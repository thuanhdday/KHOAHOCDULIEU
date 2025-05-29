import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud

# Đọc dữ liệu
df = pd.read_csv('data.csv', low_memory=False)

# Loại bỏ các dòng không có đánh giá
df.dropna(subset=['reviews.text'], inplace=True)

# Hàm phân tích cảm xúc sử dụng TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0.1:
        return 'Tích cực'
    elif analysis.sentiment.polarity < -0.1:
        return 'Tiêu cực'
    else:
        return 'Trung lập'

# Áp dụng phân tích cảm xúc vào dữ liệu
df['Cảm xúc'] = df['reviews.text'].apply(analyze_sentiment)

# ------- Biểu đồ 1: Phân phối cảm xúc -------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Cảm xúc', order=['Tích cực', 'Trung lập', 'Tiêu cực'],
              palette={'Tích cực': 'green', 'Trung lập': 'gray', 'Tiêu cực': 'red'})
plt.title('Phân phối cảm xúc trong đánh giá sản phẩm')
plt.xlabel('Loại cảm xúc')
plt.ylabel('Số lượng đánh giá')
plt.tight_layout()
plt.show()
plt.close()

# ------- Biểu đồ 2: Phân phối điểm đánh giá sao -------
if 'reviews.rating' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='reviews.rating', palette='viridis')
    plt.title('Phân phối điểm đánh giá (1-5 sao)')
    plt.xlabel('Số sao')
    plt.ylabel('Số lượng đánh giá')
    plt.tight_layout()
    plt.show()
    plt.close()

    # ------- Biểu đồ 3: Tương quan giữa điểm và cảm xúc -------
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Cảm xúc', y='reviews.rating',
                order=['Tích cực', 'Trung lập', 'Tiêu cực'],
                palette={'Tích cực': 'green', 'Trung lập': 'gray', 'Tiêu cực': 'red'})
    plt.title('Tương quan giữa điểm đánh giá và cảm xúc')
    plt.xlabel('Loại cảm xúc')
    plt.ylabel('Điểm đánh giá (sao)')
    plt.tight_layout()
    plt.show()
    plt.close()

# ------- Biểu đồ 4: Sản phẩm theo số lượng bình luận tích cực và tiêu cực (Top 10) -------
# Đếm số lượng cảm xúc theo sản phẩm
sentiment_counts = df.groupby(['name', 'Cảm xúc']).size().unstack(fill_value=0).reset_index()

# Lấy top 10 sản phẩm có nhiều đánh giá nhất
top_products = df['name'].value_counts().head(10).index
sentiment_top = sentiment_counts[sentiment_counts['name'].isin(top_products)]

# Đảm bảo các cột cảm xúc luôn tồn tại
for col in ['Tích cực', 'Tiêu cực']:
    if col not in sentiment_top.columns:
        sentiment_top[col] = 0

# Vẽ biểu đồ
fig, ax = plt.subplots(figsize=(15, 15))
sentiment_top.plot(
    x='name',
    y=['Tích cực', 'Tiêu cực'],
    kind='bar',
    stacked=True,
    ax=ax,
    colormap='coolwarm'
)
plt.title('Số lượng bình luận tích cực và tiêu cực theo sản phẩm (Top 10)', fontsize=10)
plt.xlabel('Tên sản phẩm')
plt.ylabel('Số lượng bình luận')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Loại cảm xúc')
plt.tight_layout()
plt.show()
plt.close()

# ------- WordCloud: Từ khóa phổ biến theo cảm xúc -------
# Tách văn bản và kiểm tra dữ liệu
positive_reviews = ' '.join(df[df['Cảm xúc'] == 'Tích cực']['reviews.text'].astype(str))
negative_reviews = ' '.join(df[df['Cảm xúc'] == 'Tiêu cực']['reviews.text'].astype(str))

# Kiểm tra và tạo Wordcloud cho đánh giá tích cực
if len(positive_reviews.strip()) > 0:
    try:
        wordcloud_pos = WordCloud(width=800, height=400, 
                                background_color='white', 
                                collocations=False,
                                min_word_length=3).generate(positive_reviews)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud_pos, interpolation='bilinear')
        plt.title('Từ khóa phổ biến trong đánh giá tích cực')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        plt.close()
    except Exception as e:
        print(f"Lỗi khi tạo wordcloud tích cực: {str(e)}")

# Kiểm tra và tạo Wordcloud cho đánh giá tiêu cực
if len(negative_reviews.strip()) > 0:
    try:
        wordcloud_neg = WordCloud(width=800, height=400, 
                                background_color='white', 
                                collocations=False,
                                min_word_length=3).generate(negative_reviews)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud_neg, interpolation='bilinear')
        plt.title('Từ khóa phổ biến trong đánh giá tiêu cực')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        plt.close()
    except Exception as e:
        print(f"Lỗi khi tạo wordcloud tiêu cực: {str(e)}")
